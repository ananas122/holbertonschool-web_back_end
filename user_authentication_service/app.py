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
def register_user():
    #recup de email et psw depuis les donnees de formulare
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        # Tentative d'ajout d'un nouvel user
        user = AUTH.register_user(email, password)
        # succes
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        # si mail deja enregistré 
        return jsonify({"message": "email already registered"}), 400


@ app.route('/sessions', methods=['POST'])
def login() -> str:
    """ Sessions Login User """
    try:
        email = request.form['email']
        pwd = request.form['password']
    except KeyError:
        abort(401)

    if (AUTH.valid_login(email, pwd)):
        session_id = AUTH.create_session(email)
        if session_id is not None:
            response = jsonify({"email": email, "message": "logged in"})
            response.set_cookie("session_id", session_id)
            return response
    abort(401)


@ app.route('/sessions', methods=['DELETE'])
def logout() -> str:
    """logout session"""
    session_id = request.cookies.get('session_id')

    if not session_id:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if user:
        Auth.destroy_session(user.id)
        return redirect('GET /')
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

