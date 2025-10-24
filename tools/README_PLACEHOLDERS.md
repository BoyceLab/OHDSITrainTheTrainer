# Placeholder image generator for MkDocs

This script scans your Markdown for lines like `Figure 1: Some Caption`, creates
PNG placeholders under `docs/images/`, and (optionally) injects the image links
into the Markdown so your book will render without broken images.

## Files
- `tools/mkdocs_placeholders.py`
- `tools/requirements.txt`

## Quick start (VS Code + GitHub Desktop)

```bash
# from your repo root
python -m venv .venv
# activate:
#   Windows PowerShell: .\.venv\Scripts\Activate.ps1
#   macOS/Linux:       source .venv/bin/activate

pip install -r tools/requirements.txt

# Generate placeholders from a single file and inject image links:
python tools/mkdocs_placeholders.py docs/atlas-user-process-guide.md --inject

# Or scan all markdown files in docs/ without modifying them:
python tools/mkdocs_placeholders.py docs
```

Commit the newly created images (and any modified Markdown) via GitHub Desktop.
