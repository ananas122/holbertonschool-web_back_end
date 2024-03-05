#!/usr/bin/env python3
"""task 5"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
from typing import Union

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Config class to setup Babel for English and French"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/", methods=["GET"], strict_slashes=False)
def home() -> str:
    """Template for 5-index"""
    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    """ Locale language selector function """
    user_locale = request.args.get('locale')
    if user_locale in app.config['LANGUAGES']:
        return user_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[dict, None]:
    """ Returns user dict if ID can be found """
    if request.args.get('login_as'):
        user = int(request.args.get('login_as'))
        return users.get(user)
    else:
        return None


@app.before_request
def before_request():
    """ Finds user and sets as global on flask.g.user """
    g.user = get_user()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
