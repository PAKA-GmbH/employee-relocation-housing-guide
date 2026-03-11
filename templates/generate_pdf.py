#!/usr/bin/env python3
"""Convert Stuttgart housing guide markdown to styled PDF via HTML."""

import subprocess
import sys
import re
from pathlib import Path

def md_to_html(md_text):
    """Convert markdown to HTML using Python-Markdown."""
    try:
        import markdown
        html = markdown.markdown(
            md_text,
            extensions=['tables', 'fenced_code', 'toc', 'attr_list']
        )
        return html
    except ImportError:
        # Fallback: use pandoc if available
        result = subprocess.run(
            ['pandoc', '-f', 'markdown', '-t', 'html', '--standalone'],
            input=md_text,
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            return result.stdout
        raise RuntimeError("Neither python-markdown nor pandoc available")


def build_pdf(md_path: Path, css_path: Path, output_path: Path):
    md_text = md_path.read_text(encoding='utf-8')

    # Convert markdown to HTML body
    content_html = md_to_html(md_text)

    # Read CSS
    css_content = css_path.read_text(encoding='utf-8')

    # Build full HTML document with cover page
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Stuttgart Housing Guide — PAKA GmbH</title>
  <style>
{css_content}
  </style>
</head>
<body>

<!-- COVER PAGE -->
<div class="cover">
  <div class="logo-area">
    <div class="company">PAKA GmbH &mdash; Internal HR Resource</div>
  </div>
  <h1>Stuttgart<br>Housing Guide</h1>
  <div class="subtitle">Affordable Housing Strategies for<br>International Employees</div>
  <div class="badge">Budget: €300–500/month</div>
  <div class="meta">
    Version 1.0 &bull; March 2026<br>
    Target: Young international workers relocating to Stuttgart<br>
    Research depth: Wohnheime &bull; Social Organizations &bull; Housing Portals &bull; Cooperatives
  </div>
</div>

<!-- MAIN CONTENT -->
<div class="content">
{content_html}
</div>

</body>
</html>"""

    # Save intermediate HTML
    html_path = output_path.with_suffix('.html')
    html_path.write_text(full_html, encoding='utf-8')
    print(f"HTML written: {html_path}")

    # Generate PDF with WeasyPrint
    from weasyprint import HTML, CSS
    print("Generating PDF with WeasyPrint...")
    HTML(filename=str(html_path)).write_pdf(str(output_path))
    print(f"PDF written: {output_path} ({output_path.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    base = Path(__file__).parent
    md_path = base / "stuttgart-housing-guide.md"
    css_path = base / "pdf-style.css"
    output_path = base / "Stuttgart_Housing_Guide_PAKA_GmbH.pdf"

    build_pdf(md_path, css_path, output_path)
    print("Done!")
