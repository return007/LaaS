#!/usr/bin/env python3
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

from _laas import create_leaderboard as cl

def main():
    """
    Process args and other things...
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--create', action='store_true', dest='create',
        help='Create leaderboard action.'
    )
    parser.add_argument(
        '--config', dest='config',
        help='Feed me the config file for your leaderboard view.'
    )
    parser.add_argument(
        '--output', '-o', dest='output',
        default=os.path.join(os.path.abspath('.'), 'index.html'),
        help='Path to the output leaderboard file.'
    )
    args = parser.parse_args()

    if args.create:
        # Create leaderboard using the config file
        cl(args.config, args.output)


if __name__ == '__main__':
    main()
