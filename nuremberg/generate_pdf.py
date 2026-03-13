#!/usr/bin/env python3
"""Convert Nuremberg housing guide markdown to styled PDF via HTML."""

import subprocess
import sys
from pathlib import Path

def md_to_html(md_text):
    try:
        import markdown
        html = markdown.markdown(
            md_text,
            extensions=['tables', 'fenced_code', 'toc', 'attr_list']
        )
        return html
    except ImportError:
        result = subprocess.run(
            ['pandoc', '-f', 'markdown', '-t', 'html'],
            input=md_text,
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            return result.stdout
        raise RuntimeError("Neither python-markdown nor pandoc available")


def build_pdf(md_path, css_path, output_path):
    md_text = md_path.read_text(encoding='utf-8')
    content_html = md_to_html(md_text)
    css_content = css_path.read_text(encoding='utf-8')

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Nürnberg Housing Guide</title>
  <style>
{css_content}
  </style>
</head>
<body>

<div class="cover">
  <div class="logo-area">
    <div class="company">Relocation Housing Guide</div>
  </div>
  <h1>Nürnberg<br>Housing Guide</h1>
  <div class="subtitle">Finding Your Own Pet-Friendly Apartment<br>A Practical Handbook for International Newcomers</div>
  <div class="badge">Scenarios: €600 (1 room) &bull; €1,000 (2 rooms)</div>
  <div class="meta">
    Version 1.0 &bull; March 2026<br>
    Pets allowed &bull; Own apartment &bull; Long-term stability<br>
    Portals &bull; Social Housing &bull; Cooperatives &bull; Legal Rights
  </div>
</div>

<div class="content">
{content_html}
</div>

</body>
</html>"""

    html_path = output_path.with_suffix('.html')
    html_path.write_text(full_html, encoding='utf-8')
    print(f"HTML written: {html_path}")

    from weasyprint import HTML
    print("Generating PDF...")
    HTML(filename=str(html_path)).write_pdf(str(output_path))
    print(f"PDF written: {output_path} ({output_path.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    base = Path(__file__).parent
    md_path = base / "nuremberg-housing-guide.md"
    css_path = Path(__file__).parent.parent / "templates" / "pdf-style.css"
    output_path = base / "Nuernberg_Housing_Guide.pdf"
    build_pdf(md_path, css_path, output_path)
    print("Done!")
