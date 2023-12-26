#!/usr/bin/python3
"""Start A Web Application listening on 0.0.0.0, port 5000"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Returns the Index Page"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns the 'hbnb' Page"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Returns variable page for C"""
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_magic(text='is cool'):
    """Returns variable page for python"""
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """Returns the integer variable <n>"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def is_number_template(n):
    """Displays a Html page with 'n' as an argument"""
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
