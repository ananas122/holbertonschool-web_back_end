#!/usr/bin/env python3
""" Flask module """
from flask import Flask, jsonify, request, abort, redirect, make_response
from sqlalchemy.orm.exc import NoResultFound
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def home():
    """Return a welcome message"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_user():
    # recup de email et psw depuis les donnees de formulare
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


@app.route('/sessions', methods=['POST'])
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


@app.route('/sessions', methods=['DELETE'])
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


@ app.route('/profile', methods=['GET'])
def profile() -> str:
    """ Get profile with session id
    """
    session_id = request.cookies.get('session_id', None)

    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    return jsonify({"email": user.email}), 200


@app.route('/reset_password', methods=['POST'])
def reset_password() -> str:
    """ Get profile with session id"""
    try:
        email = request.form['email']
    except KeyError:
        abort(403)

    token: str = ''
    try:
        token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)

    return jsonify({"email": email, "reset_token": token}), 200


@app.route('/reset_password', methods=['PUT'])
def update_password() -> str:
    """ Change the password"""
    try:
        email = request.form['email']
        reset_tok = request.form["reset_token"]
        new_pwd = request.form['new_password']
    except KeyError:
        abort(403)

    try:
        AUTH.update_password(reset_tok, new_pwd)
    except ValueError:
        abort(403)

    return jsonify({"email": email, "message": "Password updated"}), 200



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
