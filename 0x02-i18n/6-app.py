#!/usr/bin/env python3
""" A Basic Flask app that that translate contents
    based on user's locale using `babel_flask.Babel`
"""


from flask_babel import (
    Babel,
    gettext
)
import typing
from flask import (
    Flask,
    g,
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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_id: int) -> dict:
    """ A func that get user by the ID
    """
    # login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request():
    """ A func that runs before requests
    """
    login_id = request.args.get('login_as')
    user = get_user(login_id)
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """ A local selector to select the default language for user
    """
    local_param = g.user.get('locale')
    if local_param in app.config['LANGUAGES']:
        return local_param
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index() -> typing.Any:
    """ A simple route in the Flask App
    """
    home_title = gettext('Welcome to Holberton')
    home_header = gettext('Hello world!')
    logged_in_as = gettext("You are logged in as %(username)s.")
    not_logged_in = gettext("You are not logged in.")
    userna = g.user

    return render_template('5-index.html',
                           home_title=home_title,
                           home_header=home_header,
                           logged_in_as=logged_in_as,
                           not_logged_in=not_logged_in,
                           userna=userna
                           )


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
