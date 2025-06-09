import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


def main():
    data_path = Path('data/data.json')
    with data_path.open('r', encoding='utf-8') as f:
        data = json.load(f)

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('index_template.html')

    months_order = [
        "Ene", "Feb", "Mar", "Abr", "May", "Jun",
        "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"
    ]

    rendered = template.render(**data, months_order=months_order)
    output_path = Path('index.html')
    with output_path.open('w', encoding='utf-8') as f:
        f.write(rendered)
    print(f"Generated {output_path}")


if __name__ == '__main__':
    main()
