#!/usr/bin/env python3
"""Generic utilities for github org client.
"""
import unittest
from functools import wraps
from typing import Mapping, Sequence, Any, Dict, Callable
from parameterized import parameterized
from unittest.mock import patch
import requests

__all__ = [
    "access_nested_map",
    "get_json",
    "memoize",
]

# Classe de test pour la fonction access_nested_map


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_msg):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_msg)

# Fonction pour accéder à une valeur dans un dictionnaire en suivant un chemin donné


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """Access nested map with key path.
    Parameters
    ----------
    nested_map: Mapping
        A nested map
    path: Sequence
        a sequence of key representing a path to the value
    Example
    -------
    >>> nested_map = {"a": {"b": {"c": 1}}}
    >>> access_nested_map(nested_map, ["a", "b", "c"])
    1
    """
    # Parcours du chemin dans le dictionnaire
    for key in path:
        # Vérifie si la clé existe dans le dictionnaire
        if not isinstance(nested_map, Mapping):
            raise KeyError(key)
        nested_map = nested_map[key]

    return nested_map

# Fonction pour récupérer du JSON à partir d'une URL distante


def get_json(url: str) -> Dict:
    """Get JSON from remote URL.
    """
    response = requests.get(url)
    return response.json()

# Décorateur pour mémoriser le résultat d'une méthode


def memoize(fn: Callable) -> Callable:
    """Decorator to memoize a method.
    Example
    -------
    class MyClass:
        @memoize
        def a_method(self):
            print("a_method called")
            return 42
    >>> my_object = MyClass()
    >>> my_object.a_method
    a_method called
    42
    >>> my_object.a_method
    42
    """
    # Nom de l'attribut utilisé pour stocker le résultat mémorisé
    attr_name = "_{}".format(fn.__name__)

    @wraps(fn)
    def memoized(self):
        """"memoized wraps"""
        # Vérifie si le résultat est déjà mémorisé
        if not hasattr(self, attr_name):
            # Calcule le résultat et le mémorise
            setattr(self, attr_name, fn(self))
        # Retourne le résultat mémorisé
        return getattr(self, attr_name)

    return property(memoized)


# Point d'entrée pour exécuter les tests lorsque le script est exécuté directement
if __name__ == "__main__":
    unittest.main()
