#!/usr/bin/env python3
"""
Start the LaaS cloud server manager - called atlaas.
This fellow is a WSGI application, responsible for:

 - Hosting the HTML (the landing page of atlaas, login page, etc.)
 - Hosting the APIs (to create a new leaderboard app, update the leaderboard, etc.)
 - Managing DB (storing, retrieving, deleting entries from db)
 - Handling authorization

"""

from flask import Flask, render_template, request
from os import path


PATH_TO_WWW = path.join(
    path.dirname(path.dirname(path.abspath(__file__))),
    'www'
)


app = Flask(
    __name__,
    template_folder=PATH_TO_WWW,
    static_folder=path.join(PATH_TO_WWW, 'static')
)


def build_configuration(contents):
    return {
        "title": contents.get('event_name', 'Event Name - 2020'),
        "tabs": [
            {
                "title": contents.get('leaderboard_title', 'Leaderboard'),
                "type": contents.get('leaderboard_type', 'Ranking').lower(),
                "highlight_winners": True,
                "winners_count": 3,
                "data": "/PATH/TO/YOUR/RANKINGS/CSV/FILE",
                "event_status": "live",
                "contest_link": contents.get('event_link',
                                             'https://event.com/example')
            }
        ]
    }


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create')
def get_started():
    return render_template('step_1.html')


@app.route('/finish', methods=['POST'])
def form_submit():
    # Extract all the information from the form
    # Create config file
    # Ask user to download
    # Also instruct user to install and run laas script
    post_data = request.form
    print(post_data)
    return render_template(
        'step_2.html',
        configuration=build_configuration(post_data)
    )


if __name__ == '__main__':
    app.run("0.0.0.0")
