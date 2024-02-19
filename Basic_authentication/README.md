# Authentification et Encodage Base64

Ce projet présente une application Python pour illustrer les concepts d'authentification et d'encodage Base64. L'application utilise le module `base64` pour effectuer l'encodage et `requests` pour envoyer des requêtes HTTP.

---

## Table des matières

1. [Général](#général)
2. [Authentification](#authentification)
3. [Encodage Base64](#encodage-base64)
4. [Exemples de Code](#exemples-de-code)
5. [Conclusion](#conclusion)

---

## Général <a name="général"></a>

L'authentification est le processus par lequel un système vérifie l'identité d'un utilisateur ou d'un processus. Cela garantit que seules les personnes autorisées peuvent accéder à certaines ressources ou fonctionnalités.

Base64 est un schéma d'encodage qui permet de représenter des données binaires sous forme de chaînes de caractères ASCII. Il utilise un alphabet de 64 caractères (a-z, A-Z, 0-9, + et /) pour représenter les données binaires.

### Qu'est-ce que l'authentification de base ?

L'authentification de base est une méthode simple d'authentification HTTP où le nom d'utilisateur et le mot de passe sont envoyés sous forme d'en-tête `Authorization` dans chaque requête. Ces informations sont généralement encodées en Base64.

### Comment envoyer l'en-tête d'autorisation ?

Vous pouvez envoyer l'en-tête d'autorisation en incluant l'en-tête `Authorization` dans votre requête HTTP. Voici un exemple d'utilisation de `requests` pour envoyer une requête avec l'authentification de base :

```python
import requests
import base64

url = 'http://example.com/api/resource'
username = 'user'
password = 'password'
credentials = base64.b64encode(f"{username}:{password}".encode('utf-8')).decode('utf-8')
headers = {'Authorization': f'Basic {credentials}'}

response = requests.get(url, headers=headers)
print(response.text)

Encodage Base64 <a name="encodage-base64"></a>

***Base64 est un schéma d'encodage qui permet de représenter des données binaires sous forme de chaînes de caractères ASCII. Il est largement utilisé dans divers domaines, notamment les protocoles de communication, le stockage de données et la transmission de fichiers.***
