#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def home():
    """Return a welcome message"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users():
    #recup de eimail et psw depuis les donnees de formulare
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        # Tentative d'ajout d'un nouvel utilisateur
        user = AUTH.register_user(email, password)
        # succes
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        # si mail deja enregistré 
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
