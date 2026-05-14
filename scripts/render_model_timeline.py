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
    "core_rna_fm": "#2563eb",
    "specialized_rna_fm": "#16a34a",
    "adapted_derived": "#9333ea",
    "task_design": "#f97316",
    "related_nucleotide": "#64748b",
    "expression_profile": "#db2777",
}


def load_papers(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or []


def timeline_date(paper: dict) -> str:
    return paper.get("timeline_date", paper["date"])


def svg_text(x, y, text, size=16, weight=400, fill="#111827", anchor="middle"):
    return (
        f'<text x="{x}" y="{y}" font-family="Inter, Arial, sans-serif" '
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

    columns = 10
    rows = ceil(len(papers) / columns)
    width = 1400
    left = 86
    right = width - 86
    step_x = (right - left) / (columns - 1)
    top = 220
    tight_gap = 90
    open_gap = 132
    row_positions = row_y_positions(rows, top, tight_gap, open_gap)
    bottom_padding = 84
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
        '<rect width="100%" height="100%" fill="#fbfbfd"/>',
        svg_text(34, 42, "RNA Foundation Model Timeline", 30, 800, "#111827", "start"),
        svg_text(
            34,
            72,
            f"Auto-generated from data/papers.yaml • {len(papers)} confirmed RNA-relevant model entries",
            15,
            400,
            "#6b7280",
            "start",
        ),
    ]

    svg.append('<rect x="34" y="88" width="980" height="44" rx="8" fill="#eff6ff" stroke="#bfdbfe"/>')
    svg.append(
        svg_text(
            52,
            106,
            "Timeline dates use first public model/preprint release, not necessarily formal publication.",
            13,
            700,
            "#1d4ed8",
            "start",
        )
    )
    svg.append(
        svg_text(
            52,
            124,
            "Read each row in the arrow direction, then continue to the next row.",
            13,
            700,
            "#1d4ed8",
            "start",
        )
    )

    legend_x = width - 330
    legend_y = 31
    legend_columns = 2
    legend_rows = ceil(len(SCOPE_LABELS) / legend_columns)
    legend_col_width = 138
    legend_height = 18 + legend_rows * 22
    legend_width = legend_columns * legend_col_width + 12
    svg.append(
        f'<rect x="{legend_x - 18}" y="{legend_y - 20}" width="{legend_width}" '
        f'height="{legend_height}" rx="8" fill="#ffffff" stroke="#e5e7eb"/>'
    )
    for offset, (scope, label) in enumerate(SCOPE_LABELS.items()):
        col = offset // legend_rows
        legend_item_x = legend_x + col * legend_col_width
        y = legend_y + (offset % legend_rows) * 22
        color = SCOPE_COLORS[scope]
        svg.append(f'<circle cx="{legend_item_x}" cy="{y}" r="6" fill="{color}"/>')
        svg.append(svg_text(legend_item_x + 14, y + 5, label, 13, 500, "#374151", "start"))

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
        svg.append(f'<line x1="{row_left}" y1="{y}" x2="{row_right}" y2="{y}" stroke="#e5e7eb" stroke-width="1"/>')
        arrow = "→" if row % 2 == 0 else "←"
        arrow_x = row_left - 38 if row % 2 == 0 else row_right + 38
        svg.append(svg_text(arrow_x, y + 7, arrow, 24, 800, "#525252"))

    svg.append(
        f'<polyline points="{path_points}" fill="none" stroke="#404040" '
        'stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
    )

    label_width = 124
    label_height = 40
    for index, paper in enumerate(papers):
        x, y, row = node_position(index, columns, left, step_x, row_positions)
        scope = paper["scope"]
        color = SCOPE_COLORS.get(scope, "#64748b")
        label_y = y - 62 if row % 2 == 0 else y + 22
        line_end = label_y + label_height if row % 2 == 0 else label_y

        svg.append(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{line_end}" stroke="{color}" stroke-width="2"/>')
        svg.append(f'<circle cx="{x}" cy="{y}" r="10" fill="{color}" stroke="#ffffff" stroke-width="4"/>')
        paper_url = escape(paper.get("timeline_url", paper["paper_url"]))
        svg.append(f'<a href="{paper_url}" xlink:href="{paper_url}" target="_blank">')
        svg.append(
            f'<rect x="{x - label_width / 2}" y="{label_y}" width="{label_width}" height="{label_height}" '
            f'rx="8" fill="#ffffff" stroke="{color}" stroke-width="1.4"/>'
        )
        svg.append(svg_text(x, label_y + 15, timeline_date(paper), 11, 500, "#6b7280"))
        svg.append(svg_text(x, label_y + 30, paper["name"], 12, 700, "#111827"))
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
