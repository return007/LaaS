"""
TODO: Add documentation
"""

from util import read_config


def create_leaderboard(config_path):
    """
    Create a leaderboard for the given ``config`` file.

    :param config_path:
      `str` representing path to config file.
    """
    config = read_config(config_path)
