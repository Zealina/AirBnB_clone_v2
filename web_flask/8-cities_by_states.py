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


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
