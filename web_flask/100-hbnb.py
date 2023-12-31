#!/usr/bin/python3
"""Flask Web Application to display a list of states in storage"""
from models import storage
from flask import Flask, render_template
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def rm_current_session(exception=None):
    """Remove the current session of SQLAlchemy if db"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays an HTML page like 8-index.html"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
