# REST API Authentication Mechanisms - Authentification de session

L'authentification de session dans les API REST est un mécanisme utilisé pour maintenir l'état de l'utilisateur connecté sur plusieurs requêtes HTTP. Cela implique l'utilisation de cookies HTTP pour stocker un identifiant de session unique côté client et un suivi de l'état de l'utilisateur côté serveur. Voici une explication détaillée :

1. **Authentification initiale :** Lorsqu'un utilisateur se connecte à l'API pour la première fois, il fournit ses informations d'identification (nom d'utilisateur, mot de passe, etc.). Le serveur vérifie ces informations et, si elles sont valides, crée une session pour l'utilisateur.

2. **Création du cookie de session :** Une fois la session créée, le serveur génère un identifiant de session unique (généralement une chaîne de caractères aléatoires) et l'associe à cet utilisateur. Ce jeton de session est ensuite stocké dans un cookie HTTP.

3. **Envoi du cookie au client :** Lorsque le serveur envoie la réponse à la demande d'authentification réussie, il inclut le cookie de session dans l'en-tête de la réponse HTTP. Le client (navigateur web, application mobile, etc.) stocke alors ce cookie localement.

4. **Utilisation du cookie pour les requêtes ultérieures :** Lorsque le client effectue des requêtes ultérieures à l'API, le navigateur envoie automatiquement le cookie de session stocké dans ses en-têtes HTTP. Le serveur peut alors vérifier ce cookie pour identifier l'utilisateur et autoriser l'accès aux ressources protégées.

5. **Expiration et invalidation des sessions :** Les cookies de session ont généralement une durée de vie limitée, définie par le serveur. Une fois cette durée écoulée ou si l'utilisateur se déconnecte explicitement, le serveur invalide le cookie de session, obligeant l'utilisateur à se reconnecter pour continuer à accéder aux ressources protégées.

# HTTP Cookie

Un cookie HTTP est un petit fichier texte stocké par le navigateur web d'un utilisateur sur son ordinateur. Il est utilisé pour stocker des informations telles que des identifiants de session, des préférences utilisateur, des données de suivi, etc. Les cookies sont envoyés entre le navigateur et le serveur avec chaque requête HTTP, permettant au serveur de maintenir un état de session pour chaque utilisateur.

# Flask et Flask Cookie

Flask est un framework web léger pour Python, souvent utilisé pour développer des applications web et des API REST. Flask offre un support intégré pour la gestion des cookies à l'aide de la bibliothèque Werkzeug.

Voici un exemple complet de création et d'utilisation de cookies dans Flask :

```python
from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/')
def index():
    # Création d'un cookie
    response = make_response('Cookie créé et envoyé !')
    response.set_cookie('nom_cookie', 'valeur_cookie')
    return response

@app.route('/lire_cookie')
def lire_cookie():
    # Lecture d'un cookie
    nom_cookie = request.cookies.get('nom_cookie')
    return f'Contenu du cookie nom_cookie : {nom_cookie}'

if __name__ == '__main__':
    app.run(debug=True)
