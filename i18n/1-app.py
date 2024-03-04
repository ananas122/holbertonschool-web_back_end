#!/usr/bin/env python3
""" 
module task 1
"""

from flask import Flask
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

# Configuration des langues disponibles dans l'application
app.config['LANGUAGES'] = {
    'en': 'English',
    'fr': 'French'
}


@babel.localeselector
def get_locale():
    # Fonction de rappel pour déterminer la langue à utiliser
    return 'fr'  


if __name__ == "__main__":
    app.run(debug=True)
