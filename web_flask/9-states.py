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
def states():
    """Displays an HTML page with a list of all States"""
    states = storage.all(State)
    return render_template("9-states.html", states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Display the states whose Id is supplied as variable"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
