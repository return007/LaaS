#!/usr/bin/env python3
"""
Start the LaaS cloud server manager - called atlaas.
This fellow is a WSGI application, responsible for:

 - Hosting the HTML (the landing page of atlaas, login page, etc.)
 - Hosting the APIs (to create a new leaderboard app, update the leaderboard, etc.)
 - Managing DB (storing, retrieving, deleting entries from db)
 - Handling authorization

"""

from flask import Flask, render_template
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


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run("0.0.0.0")
