"""Convert Markdown (.md) content files to Jupyter notebooks (.ipynb).

Splits on ## headings, turns Python code fences into code cells,
and preserves all MyST directives and LaTeX math in markdown cells.
"""

import json
import re
from pathlib import Path

NOTES = Path(__file__).resolve().parent.parent / "notes"

# All .md content files to convert (relative to notes/)
MD_FILES = [
    "content/intro.md",
    "content/zbibliography.md",
    "content/contributing.md",
    "content/first-order.md",
    "content/Geometry.md",
    "content/LinearAlgebra.md",
    "content/NumberTheory.md",
    "content/second-order/second-order.md",
    "content/second-order/power-series.md",
    "content/bvps/boundary-value-problems.md",
    "content/pdes/partial-differential-equations.md",
    "content/pdes/hyperbolic.md",
]

NOTEBOOK_METADATA = {
    "kernelspec": {
        "display_name": "Python 3 (ipykernel)",
        "language": "python",
        "name": "python3",
    },
    "language_info": {
        "name": "python",
        "version": "3.11.0",
    },
}


def _make_markdown_cell(source: str) -> dict:
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": source.splitlines(keepends=True),
    }


def _make_code_cell(source: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": source.splitlines(keepends=True),
    }


def _split_into_cells(text: str) -> list[dict]:
    """Split markdown text into notebook cells.

    • Python code fences (```python ... ```) become code cells.
    • Everything else stays as markdown cells, split at ## headings.
    """
    cells: list[dict] = []

    # First pass: separate code blocks from prose
    # Pattern matches ```python ... ``` blocks
    code_pattern = re.compile(
        r"```python\s*\n(.*?)```", re.DOTALL
    )

    parts: list[tuple[str, str]] = []  # (type, content)
    last_end = 0
    for m in code_pattern.finditer(text):
        # markdown before this code block
        md_before = text[last_end : m.start()]
        if md_before.strip():
            parts.append(("md", md_before))
        parts.append(("code", m.group(1)))
        last_end = m.end()
    # trailing markdown
    md_after = text[last_end:]
    if md_after.strip():
        parts.append(("md", md_after))

    # Second pass: split markdown parts at ## headings
    for kind, content in parts:
        if kind == "code":
            cells.append(_make_code_cell(content.strip()))
        else:
            # Split at lines starting with ## (but not ### etc. which we keep together)
            # Actually split at any ##+ heading for big files, or just ## for smaller.
            # Let's split at ## to keep cells manageable.
            sections = re.split(r"(?=^## )", content, flags=re.MULTILINE)
            for sec in sections:
                sec = sec.strip()
                if sec:
                    cells.append(_make_markdown_cell(sec))

    return cells


def convert(md_path: Path) -> None:
    text = md_path.read_text(encoding="utf-8")

    cells = _split_into_cells(text)
    if not cells:
        cells = [_make_markdown_cell("")]

    notebook = {
        "cells": cells,
        "metadata": NOTEBOOK_METADATA,
        "nbformat": 4,
        "nbformat_minor": 5,
    }

    out_path = md_path.with_suffix(".ipynb")
    out_path.write_text(
        json.dumps(notebook, indent=1, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"  ✓ {md_path.relative_to(NOTES)} → {out_path.relative_to(NOTES)}")


def main() -> None:
    print("Converting .md → .ipynb …")
    for rel in MD_FILES:
        md_path = NOTES / rel
        if not md_path.exists():
            print(f"  ✗ {rel} — not found, skipping")
            continue
        convert(md_path)
    print("Done.")


if __name__ == "__main__":
    main()
