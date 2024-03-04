# Projet d'Internationalisation (i18n)

Ce projet est une démonstration de l'utilisation de l'internationalisation (i18n) pour rendre une application compatible avec différentes langues et cultures.

## Fonctionnalités

- Support de plusieurs langues : anglais, français, espagnol.
- Gestion dynamique du contenu en fonction de la langue sélectionnée.
- Implémentation de chaînes de traduction pour chaque langue supportée.
- Détection automatique de la langue du navigateur de l'utilisateur.

## Technologies utilisées

- React : bibliothèque JavaScript pour la construction d'interfaces utilisateur.
- react-i18next : bibliothèque de gestion de l'internationalisation pour React.
- HTML/CSS : langages de base pour la structuration et la mise en page des pages web.

## Configuration

1. Cloner le dépôt : `git clone https://github.com/votre_utilisateur/projet-i18n.git`
2. Installer les dépendances : `npm install`
3. Démarrer l'application : `npm start`

## Structure du Projet

app.config['LANGUAGES'] = {
    'en': 'English',
    'fr': 'French',
    'es': 'Spanish'
}
app.config['BABEL_TRANSLATION_DIRECTORIES'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'translations')

gettext
