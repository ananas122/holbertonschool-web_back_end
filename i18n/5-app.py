#!/usr/bin/env python3
"""
Paramétrer les modèles
"""
import flask
from flask import Flask, render_template, g, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)

# Utilisateurs fictifs
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

# Configuration de Babel


class Config(object):
    """
    Configuration de l'application
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route("/", methods=['GET'])
def index():
    """
    Rendre le modèle avec les informations utilisateur appropriées
    """
    return render_template('5-index.html')


def get_user() -> dict:
    """Retrieve user based on login_as parameter"""
    # Get the value of the login_as prm from the request's query prm
    user_id = request.args.get('login_as')
    try:
        # Try to convert the user_id to an integer
        user_id = int(user_id)
        # Check if the user_id exists in the users dictionary
        if user_id in users:
            # Return the user dictionary corresponding to the user_id
            return users[user_id]
    # if there's an error during conversion or if user_id is not found in users
    except (ValueError, TypeError):
        # If there's an error, do nothing and proceed to the next step
        pass
    # If user_id is not found or there's an error
    return None


@app.before_request
def before_request():
    """
    Définir l'utilisateur global s'il est connecté
    """
    user = get_user()
    if user:
        g.user = user


@babel.localeselector
def get_locale():
    """
    Déterminer la langue préférée de l'utilisateur
    """
    requested_locale = request.args.get('locale')
    if requested_locale in Config.LANGUAGES:
        return requested_locale

    return request.accept_languages.best_match(Config.LANGUAGES)
