#!/usr/bin/env python3
"""Render a Markdown file's ```mermaid blocks to PNGs for Confluence.

Confluence Cloud has no native Mermaid rendering. md2cf uploads a ```mermaid
fence as a plain code block, so diagrams show as source. This script pre-renders
each block to a PNG (via mermaid-cli) and rewrites the block into an image
reference. md2cf then uploads those local PNGs as page attachments.

Usage:
    python render-mermaid.py INPUT.md OUTPUT_DIR

Writes OUTPUT_DIR/<name>.md plus diagram-N.png beside it. Publish that copy:
    uvx md2cf -A <parent-id> -t "Title" OUTPUT_DIR/<name>.md

Requires `npx` (renders with `@mermaid-js/mermaid-cli`, downloaded on first run).
"""

import subprocess
import sys
from pathlib import Path

FENCE = "```"


def split_mermaid_blocks(text: str) -> tuple[str, list[str]]:
    """Replace each ```mermaid block with an image placeholder token.

    Returns the rewritten text (blocks swapped for `{{MERMAID:N}}` tokens) and
    the list of extracted diagram sources, in document order.
    """
    lines = text.splitlines()
    out: list[str] = []
    blocks: list[str] = []
    i = 0
    while i < len(lines):
        if lines[i].strip() == f"{FENCE}mermaid":
            body: list[str] = []
            i += 1
            while i < len(lines) and lines[i].strip() != FENCE:
                body.append(lines[i])
                i += 1
            i += 1  # skip closing fence
            out.append(f"{{{{MERMAID:{len(blocks)}}}}}")
            blocks.append("\n".join(body))
        else:
            out.append(lines[i])
            i += 1
    return "\n".join(out), blocks


def render(source: str, out_png: Path) -> None:
    """Render one mermaid source string to a white-background PNG."""
    mmd = out_png.with_suffix(".mmd")
    mmd.write_text(source, encoding="utf-8")
    # -b white: opaque background; -s 2: 2x scale for legible text on Confluence.
    subprocess.run(
        ["npx", "-y", "@mermaid-js/mermaid-cli", "-i", str(mmd),
         "-o", str(out_png), "-b", "white", "-s", "2"],
        check=True,
    )


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit("usage: render-mermaid.py INPUT.md OUTPUT_DIR")
    src = Path(sys.argv[1])
    out_dir = Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)

    text, blocks = split_mermaid_blocks(src.read_text(encoding="utf-8"))
    if not blocks:
        print("no mermaid blocks found")
    for n, block in enumerate(blocks):
        png = out_dir / f"diagram-{n}.png"
        render(block, png)
        text = text.replace(f"{{{{MERMAID:{n}}}}}", f"![diagram {n}](diagram-{n}.png)")
        print(f"rendered diagram-{n}.png")

    out_md = out_dir / src.name
    out_md.write_text(text, encoding="utf-8")
    print(f"wrote {out_md}")


if __name__ == "__main__":
    main()
