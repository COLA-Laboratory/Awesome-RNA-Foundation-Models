"""Render the README model timeline SVG from data/papers.yaml."""
from __future__ import annotations

from math import ceil
from pathlib import Path
from xml.sax.saxutils import escape

import yaml


ROOT = Path(__file__).resolve().parents[1]
PAPERS_FILE = ROOT / "data" / "papers.yaml"
OUTPUT_FILE = ROOT / "assets" / "model_timeline.svg"

SCOPE_LABELS = {
    "core_rna_fm": "Core",
    "specialized_rna_fm": "Specialized",
    "adapted_derived": "Adapted",
    "task_design": "Task/Design",
    "related_nucleotide": "DNA+RNA",
    "expression_profile": "Expression",
}

SCOPE_COLORS = {
    "core_rna_fm": "#2f6fff",
    "specialized_rna_fm": "#00c878",
    "adapted_derived": "#a855ff",
    "task_design": "#ff6a22",
    "related_nucleotide": "#7a889b",
    "expression_profile": "#ff3f7f",
}


def load_papers(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or []


def timeline_date(paper: dict) -> str:
    return paper.get("timeline_date", paper["date"])


def svg_text(x, y, text, size=16, weight=400, fill="#111827", anchor="middle"):
    return (
        f'<text x="{x}" y="{y}" font-family="SFMono-Regular, Menlo, Monaco, Consolas, monospace" '
        f'font-size="{size}" font-weight="{weight}" fill="{fill}" '
        f'text-anchor="{anchor}">{escape(str(text))}</text>'
    )


def row_y_positions(rows: int, top: int, tight_gap: int, open_gap: int) -> list[int]:
    positions = [top]
    for row in range(1, rows):
        previous_row = row - 1
        gap = tight_gap if previous_row % 2 == 0 else open_gap
        positions.append(positions[-1] + gap)
    return positions


def node_position(index: int, columns: int, left: int, step_x: int, row_positions: list[int]):
    row = index // columns
    col = index % columns
    if row % 2:
        col = columns - 1 - col
    return left + col * step_x, row_positions[row], row


def render_timeline_svg(input_file: Path = PAPERS_FILE, output_file: Path = OUTPUT_FILE) -> None:
    papers = sorted(load_papers(input_file), key=lambda record: timeline_date(record))

    columns = 9
    rows = ceil(len(papers) / columns)
    width = 1400
    left = 100
    right = width - 100
    step_x = (right - left) // (columns - 1)
    top = 286
    tight_gap = 104
    open_gap = 144
    row_positions = row_y_positions(rows, top, tight_gap, open_gap)
    bottom_padding = 96
    height = row_positions[-1] + bottom_padding

    points = [
        node_position(index, columns, left, step_x, row_positions)[:2]
        for index, _ in enumerate(papers)
    ]
    path_points = " ".join(f"{x},{y}" for x, y in points)

    svg = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
        f'width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        "<defs>",
        '<radialGradient id="heroGlow" cx="18%" cy="17%" r="58%">',
        '<stop offset="0%" stop-color="#2a0509" stop-opacity="0.95"/>',
        '<stop offset="46%" stop-color="#160305" stop-opacity="0.54"/>',
        '<stop offset="100%" stop-color="#030303" stop-opacity="0"/>',
        "</radialGradient>",
        '<linearGradient id="titleAccent" x1="0%" y1="0%" x2="100%" y2="0%">',
        '<stop offset="0%" stop-color="#ff7a22"/>',
        '<stop offset="55%" stop-color="#ff4f7f"/>',
        '<stop offset="100%" stop-color="#22d3ee"/>',
        "</linearGradient>",
        '<filter id="nodeGlow" x="-80%" y="-80%" width="260%" height="260%">',
        '<feGaussianBlur stdDeviation="3.2" result="blur"/>',
        '<feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>',
        "</filter>",
        "</defs>",
        '<rect width="100%" height="100%" fill="#030303"/>',
        '<rect width="100%" height="100%" fill="url(#heroGlow)"/>',
        '<line x1="0" y1="1" x2="1400" y2="1" stroke="#242424" stroke-width="1"/>',
        f'<line x1="0" y1="{height - 1}" x2="1400" y2="{height - 1}" stroke="#242424" stroke-width="1"/>',
        '<text x="96" y="68" font-family="SFMono-Regular, Menlo, Monaco, Consolas, monospace" '
        'font-size="11" font-weight="500" fill="#7a7a7a" letter-spacing="7" text-anchor="start">MODEL ATLAS</text>',
        '<text x="96" y="112" font-family="SFMono-Regular, Menlo, Monaco, Consolas, monospace" '
        'font-size="34" font-weight="700" fill="#f8fafc" text-anchor="start">RNA Foundation</text>',
        '<text x="96" y="152" font-family="SFMono-Regular, Menlo, Monaco, Consolas, monospace" '
        'font-size="34" font-weight="700" fill="url(#titleAccent)" text-anchor="start">Model Timeline</text>',
        svg_text(
            96,
            184,
            f"Auto-generated from data/papers.yaml • {len(papers)} confirmed RNA-relevant model entries",
            13,
            400,
            "#a3a3a3",
            "start",
        ),
    ]

    svg.append('<rect x="96" y="202" width="760" height="44" rx="4" fill="#090909" stroke="#252525"/>')
    svg.append('<rect x="96" y="202" width="3" height="44" rx="1.5" fill="url(#titleAccent)"/>')
    svg.append(
        svg_text(
            116,
            221,
            "Timeline dates use first public model/preprint release, not necessarily formal publication.",
            12,
            700,
            "#e5e7eb",
            "start",
        )
    )
    svg.append(
        svg_text(
            116,
            237,
            "Read each row in the arrow direction, then continue to the next row.",
            12,
            700,
            "#8f8f8f",
            "start",
        )
    )

    legend_x = width - 292
    legend_y = 54
    legend_columns = 2
    legend_rows = ceil(len(SCOPE_LABELS) / legend_columns)
    legend_col_width = 112
    legend_height = 18 + legend_rows * 22
    legend_width = legend_columns * legend_col_width + 34
    svg.append(
        f'<rect x="{legend_x - 22}" y="{legend_y - 25}" width="{legend_width}" '
        f'height="{legend_height + 14}" rx="10" fill="#080808" stroke="#222222"/>'
    )
    for offset, (scope, label) in enumerate(SCOPE_LABELS.items()):
        col = offset // legend_rows
        legend_item_x = legend_x + col * legend_col_width
        y = legend_y + (offset % legend_rows) * 22
        color = SCOPE_COLORS[scope]
        svg.append(f'<circle cx="{legend_item_x}" cy="{y}" r="5.5" fill="{color}" filter="url(#nodeGlow)"/>')
        svg.append(svg_text(legend_item_x + 16, y + 5, label, 12, 500, "#d4d4d4", "start"))

    for row in range(rows):
        row_points = [
            node_position(index, columns, left, step_x, row_positions)[:2]
            for index in range(len(papers))
            if index // columns == row
        ]
        if not row_points:
            continue
        y = row_positions[row]
        row_left = min(x for x, _ in row_points)
        row_right = max(x for x, _ in row_points)
        svg.append(f'<line x1="{row_left}" y1="{y}" x2="{row_right}" y2="{y}" stroke="#151515" stroke-width="1"/>')
        arrow = "→" if row % 2 == 0 else "←"
        arrow_x = row_left - 38 if row % 2 == 0 else row_right + 38
        svg.append(svg_text(arrow_x, y + 7, arrow, 22, 800, "#747474"))

    svg.append(
        f'<polyline points="{path_points}" fill="none" stroke="#404040" '
        'stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>'
    )

    label_width = 136
    label_height = 42
    for index, paper in enumerate(papers):
        x, y, row = node_position(index, columns, left, step_x, row_positions)
        scope = paper["scope"]
        color = SCOPE_COLORS.get(scope, "#64748b")
        label_y = y - 68 if row % 2 == 0 else y + 26
        line_end = label_y + label_height if row % 2 == 0 else label_y

        svg.append(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{line_end}" stroke="{color}" stroke-width="2"/>')
        svg.append(f'<circle cx="{x}" cy="{y}" r="9.5" fill="{color}" stroke="#050505" stroke-width="4" filter="url(#nodeGlow)"/>')
        paper_url = escape(paper.get("timeline_url", paper["paper_url"]))
        svg.append(f'<a href="{paper_url}" xlink:href="{paper_url}" target="_blank">')
        svg.append(
            f'<rect x="{x - label_width / 2}" y="{label_y}" width="{label_width}" height="{label_height}" '
            f'rx="7" fill="#070707" stroke="{color}" stroke-width="1.35"/>'
        )
        svg.append(svg_text(x, label_y + 15, timeline_date(paper), 10, 500, "#8f8f8f"))
        svg.append(svg_text(x, label_y + 31, paper["name"], 12, 700, "#f8fafc"))
        svg.append("</a>")

    svg.append("</svg>")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text("\n".join(svg) + "\n", encoding="utf-8")


def main() -> int:
    render_timeline_svg()
    print(f"Wrote {OUTPUT_FILE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
