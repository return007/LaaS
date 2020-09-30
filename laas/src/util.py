"""
Utility functions
"""

import csv
import json
import os


def read_config(config_path):
    try:
        with open(config_path, 'r') as cfg:
            config = json.load(cfg)
    except Exception:
        print('Error while reading config from path: "%s"' % config_path)
        raise
    return config


def _read_template(template_type='index'):
    """
    Which template to read from pre-defined set of templates.

    :param template_type:
      One of ``index``, ``hall_of_fame`` or ``ranking``.
    """
    assert template_type in ('index', 'hall_of_fame', 'ranking')
    tmpl_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tmpl_path = os.path.join(tmpl_path, 'template')
    with open(os.path.join(tmpl_path, '%s.html' % template_type), 'r') as f:
        return f.read()


def _read_csv(path):
    """
    Read csv data from file indicated via ``path``.
    """
    data = []
    with open(path, 'r') as f:
        _itr = csv.reader(f)
        for line in _itr:
            data.append(line)
    return data
