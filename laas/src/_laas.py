"""
TODO: Add documentation
"""

import sys

from jinja2 import Template
from util import read_config, _read_template, _read_csv


def _create_table():
    pass


def create_leaderboard(config_path, output_path):
    """
    Create a leaderboard for the given ``config`` file.

    :param config_path:
      `str` representing path to config file.
    """
    config = read_config(config_path)

    title = config.get('title', '')
    if not title:
        print("Leaderboard title is mandatory. Please provide the same in "
              "your config file")
        sys.exit(1)

    tabs = config.get('tabs', [])
    pills = []
    for i, tab in enumerate(tabs):
        pill = {
            'pill_id': 'pill%d' % i,
            'status': 'active' if i == 0 else '',
            'nav_id': 'tab%d' % i,
            'title': tab['title']
        }
        pills.append(pill)

    tables = []
    for i, tab in enumerate(tabs):
        table = {
            'status': 'show active' if i == 0 else '',
            'nav_id': 'tab%d' % i,
            'pill_id': 'pill%d' % i,
            'type': tab['type'],
            'table': ''
        }
        data = _read_csv(tab['data'])
        print(len(data))
        tmpl = Template(_read_template(tab['type']))
        tbl_html = tmpl.render(data=data)
        table['table'] = tbl_html
        tables.append(table)

    index_tmpl = Template(_read_template('index'))
    index_html = index_tmpl.render(title=title, pills=pills,
                                   tables=tables)

    with open(output_path, 'w') as f:
        f.write(index_html)
