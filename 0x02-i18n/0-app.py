#!/usr/bin/env python3
""" A Basic Flask app that renders 0-index.html template
"""


import typing
from flask import (
    Flask,
    render_template
)


# Initialize a flask app
app = Flask(__name__)


@app.route("/")
def home() -> typing.Any:
    """ A simple route in the Flask App
    """
    return render_template('0-index.html')
