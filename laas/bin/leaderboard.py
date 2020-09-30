"""
Process config files and CSV data to create beautiful static leaderboard pages
which can be self hosted.

Sounds like a "Leaderboard-as-a-Service".

:author: return007
:date: 2020-09-30
"""

import argparse
import os
import sys

SRC_PATH = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.append(os.path.join(SRC_PATH, 'src'))

from _lass import create_leaderboard as cl

def main():
    """
    Process args and other things...
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '--create', action='store_true', dest='create',
        help='Create leaderboard action.'
    )
    parser.add_argument(
        '--config', nargs=1, dest='config',
        help='Feed me the config file for your leaderboard view.'
    )
    args = parser.parse_args()

    if args.create:
        # Create leaderboard using the config file
        cl(config)


if __name__ == '__main__':
    main()
