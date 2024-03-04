#!/usr/bin/env python3
""" 
module
"""

from flask import Flask, render_template

# Création de l'application Flask
app = Flask(__name__)

# Configuration des langues disponibles dans l'application
app.config['LANGUAGES'] = {
    'en': 'English',
    'fr': 'French'
}

# Configuration de la langue par défaut et du fuseau horaire
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


@app.route('/')
def index():
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
