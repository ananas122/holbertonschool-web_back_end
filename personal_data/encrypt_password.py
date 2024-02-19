#!/usr/bin/env python3
"""
Task 5. Encrypting passwords
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Generate a secure hash of the given password."""
    # Convertir le mot de passe en tableau de bytes
    password_bytes = password.encode('utf-8')

    # Générer le sel
    salt = bcrypt.gensalt()

    # Hacher le mot de passe
    hashed_password = bcrypt.hashpw(password_bytes, salt)

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Returns a hashed password """
    # bcrypt.checkpw pr vérifier si le mot de passe = au hachage stocké.
    # password.encode('utf-8') convertit le mot de passe fourni en bytes.
    # hashed_password est le hachage de mot de passe stocké.
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
