# Auditor Trading

This project generates a simple static site from template data.

## Usage

1. Edit the values in `data/data.json` to update dashboard numbers, monthly returns and statistics.
2. Run `python scripts/generate_site.py` to render `templates/index_template.html` into `index.html`.

The script requires [Jinja2](https://palletsprojects.com/p/jinja/) which can be installed with:

```bash
pip install jinja2
```
