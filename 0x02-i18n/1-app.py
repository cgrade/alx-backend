#!/usr/bin/env python3
""" A Basic Flask app that renders 0-index.html template
"""


from flask_babel import Babel
import typing
from flask import (
    Flask,
    render_template,
    request
)


# Initialize a flask app
app = Flask(__name__)
babel = Babel(app)


class Config:
    """ A class that configures available languages in our app
    """
    LANGUAGES = ["en", "fr"]


@babel.localeselector
def get_locale():
    """ A local selector to select the default language for user
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def home() -> typing.Any:
    """ A simple route in the Flask App
    """
    return render_template('0-index.html')
