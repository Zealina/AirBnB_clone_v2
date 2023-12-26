#!/usr/bin/python3
"""Start A Web Application listening on 0.0.0.0, port 5000"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Returns the Index Page"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns the 'hbnb' Page"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
