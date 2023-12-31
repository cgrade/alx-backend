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


class Config:
    """ A class that configures available languages in our app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Initialize a flask app
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ A local selector to select the default language for user
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index() -> typing.Any:
    """ A simple route in the Flask App
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
