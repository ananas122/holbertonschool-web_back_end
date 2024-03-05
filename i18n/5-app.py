#!/usr/bin/env python3
"""Task 5: Mock logging in"""

# Import des modules Flask et Babel
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
from typing import Union


# Initialisation de l'application Flask
app = Flask(__name__)
babel = Babel(app)


# Mockup de la table des utilisateurs
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


# Configuration de Babel pour les langues
class Config(object):
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Application de la configuration à l'application Flask
app.config.from_object(Config)


# Route pour la page d'accueil
@app.route("/", methods=["GET"], strict_slashes=False)
def home():
    """Template for 5-index"""
    return render_template('5-index.html')


# Sélecteur de locale pour Babel
@babel.localeselector
def get_locale():
    """ Locale language"""
    locale = request.args.get('locale', None)
    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


# Fonction pour récupérer l'utilisateur
def get_user() -> dict:
    """get user"""
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


# Fonction exécutée avant chaque requête
@app.before_request
def before_request():
    """ Finds user and sets as global on flask.g.user """
    g.user = get_user()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
