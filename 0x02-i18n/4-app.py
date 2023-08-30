#!/usr/bin/env python3
""" A Basic Flask app that renders 0-index.html template
"""


from flask_babel import (
    Babel,
    gettext
)
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
def get_locale() -> str:
    """ A local selector to select the default language for user
    """
    local_param = request.args.get('locale')
    if local_param in app.config['LANGUAGES']:
        return local_param
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index() -> typing.Any:
    """ A simple route in the Flask App
    """
    home_title = gettext('Welcome to Holberton')
    home_header = gettext('Hello world!')
    return render_template('4-index.html',
                           home_title=home_title, home_header=home_header)


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
