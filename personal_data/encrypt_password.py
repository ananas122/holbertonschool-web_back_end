#!/usr/bin/env python3
"""
Task 5. Encrypting passwords
"""

#!/usr/bin/env python3
import bcrypt


def hash_password(password):
    """Generate a secure hash of the given password."""
    # Convertir le mot de passe en tableau de bytes
    password_bytes = password.encode('utf-8')

    # Générer le sel
    salt = bcrypt.gensalt()

    # Hacher le mot de passe
    hashed_password = bcrypt.hashpw(password_bytes, salt)

    return hashed_password
