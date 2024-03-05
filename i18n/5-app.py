#!/usr/bin/env python3
"""
Parametrize templates
"""
import flask
from flask import Flask, render_template, g, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


users = {
    USER_BALOU: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    USER_BEYONCE: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    USER_SPOCK: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    USER_TELETUBBY: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """
    a configuration variable
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


def get_user() -> dict:
    """
    Retrieve user based on login_as parameter
    """
    user_id = request.args.get('login_as')
    try:
        user_id = int(user_id)
        if user_id in users:
            return users[user_id]
    except (ValueError, TypeError):
        pass
    return None


@app.before_request
def before_request():
    """
    Set the global user object if logged in
    """
    user = get_user()
    if user:
        g.user = user


@babel.localeselector
def get_locale():
    """
    Determine the user's preferred locale
    """
    requested_locale = request.args.get('locale')
    if requested_locale in Config.LANGUAGES:
        return requested_locale

    return request.accept_languages.best_match(Config.LANGUAGES)


app.config.from_object(Config)


@app.route("/", methods=['GET'])
def hello_world():
    """
    Render the template with the appropriate user information
    """
    return render_template('5-index.html')
