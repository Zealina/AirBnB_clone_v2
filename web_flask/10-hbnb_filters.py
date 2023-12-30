#!/usr/bin/python3
"""Flask Web Application to display a list of states in storage"""
from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def rm_current_session(exception=None):
    """Remove the current session of SQLAlchemy if db"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Display a html page consisting of multiple files"""


if __name__ == '__main__':
    app.run(host='0.0.0.0')
