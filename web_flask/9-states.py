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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=""):
    """Display the states whose Id is supplied as variable"""
    states = storage.all(State)
    return render_template("9-states.html", states=states, id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
