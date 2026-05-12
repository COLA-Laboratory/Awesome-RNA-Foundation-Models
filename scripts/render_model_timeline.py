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
}

SCOPE_COLORS = {
    "core_rna_fm": "#2563eb",
    "specialized_rna_fm": "#16a34a",
    "adapted_derived": "#9333ea",
}


def load_papers(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or []


def svg_text(x, y, text, size=16, weight=400, fill="#111827", anchor="middle"):
    return (
        f'<text x="{x}" y="{y}" font-family="Inter, Arial, sans-serif" '
        f'font-size="{size}" font-weight="{weight}" fill="{fill}" '
        f'text-anchor="{anchor}">{escape(str(text))}</text>'
    )


def node_position(index: int, columns: int, left: int, step_x: int, top: int, step_y: int):
    row = index // columns
    col = index % columns
    if row % 2:
        col = columns - 1 - col
    return left + col * step_x, top + row * step_y, row


def render_timeline_svg(input_file: Path = PAPERS_FILE, output_file: Path = OUTPUT_FILE) -> None:
    papers = sorted(load_papers(input_file), key=lambda record: record["date"])

    columns = 9
    rows = ceil(len(papers) / columns)
    width = 1400
    left = 90
    right = width - 90
    step_x = (right - left) // (columns - 1)
    top = 168
    step_y = 156
    bottom_padding = 90
    height = top + (rows - 1) * step_y + bottom_padding

    points = [
        node_position(index, columns, left, step_x, top, step_y)[:2]
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
            f"Auto-generated from data/papers.yaml • {len(papers)} confirmed RNA sequence foundation models",
            15,
            400,
            "#6b7280",
            "start",
        ),
    ]

    legend_x = width - 330
    legend_y = 31
    svg.append(f'<rect x="{legend_x - 18}" y="{legend_y - 20}" width="290" height="72" rx="8" fill="#ffffff" stroke="#e5e7eb"/>')
    for offset, (scope, label) in enumerate(SCOPE_LABELS.items()):
        y = legend_y + offset * 22
        color = SCOPE_COLORS[scope]
        svg.append(f'<circle cx="{legend_x}" cy="{y}" r="6" fill="{color}"/>')
        svg.append(svg_text(legend_x + 14, y + 5, label, 13, 500, "#374151", "start"))

    for row in range(rows):
        y = top + row * step_y
        svg.append(f'<line x1="{left}" y1="{y}" x2="{right}" y2="{y}" stroke="#e5e7eb" stroke-width="1"/>')

    svg.append(
        f'<polyline points="{path_points}" fill="none" stroke="#404040" '
        'stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
    )

    label_width = 136
    label_height = 42
    for index, paper in enumerate(papers):
        x, y, row = node_position(index, columns, left, step_x, top, step_y)
        scope = paper["scope"]
        color = SCOPE_COLORS.get(scope, "#64748b")
        label_y = y - 68 if row % 2 == 0 else y + 26
        line_end = label_y + label_height if row % 2 == 0 else label_y

        svg.append(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{line_end}" stroke="{color}" stroke-width="2"/>')
        svg.append(f'<circle cx="{x}" cy="{y}" r="10" fill="{color}" stroke="#ffffff" stroke-width="4"/>')
        paper_url = escape(paper["paper_url"])
        svg.append(f'<a href="{paper_url}" xlink:href="{paper_url}">')
        svg.append(
            f'<rect x="{x - label_width / 2}" y="{label_y}" width="{label_width}" height="{label_height}" '
            f'rx="8" fill="#ffffff" stroke="{color}" stroke-width="1.4"/>'
        )
        svg.append(svg_text(x, label_y + 16, paper["date"], 11, 500, "#6b7280"))
        svg.append(svg_text(x, label_y + 32, paper["name"], 13, 700, "#111827"))
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
