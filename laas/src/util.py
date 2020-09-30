"""
Utility functions
"""

import json


def read_config(config_path):
    try:
        with open(config_path, 'r') as cfg:
            config = json.loads(cfg)
    except Exception:
        print('Error while reading config from path: "%s"' % config_path)
        raise
    return config
