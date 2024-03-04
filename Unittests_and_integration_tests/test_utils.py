#!/usr/bin/env python3
"""first unit test"""
# Import des modules nécessaires
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from typing import Mapping, Sequence
from unittest.mock import patch
from unittest import mock

# Classe de test pour la fonction access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class"""

    @parameterized.expand([
        ({'a': 1}, ['a'], 1),
        ({'a': {'b': 2}}, ['a'], {'b': 2}),
        ({'a': {'b': 2}}, ['a', 'b'], 2),
    ])
    def test_access_nested_map(self, input_data, path, expected_result):
        """Test access_nested_map function"""
        # Vérifie que la fonction renvoie le résultat attendu
        self.assertEqual(access_nested_map(input_data, path), expected_result)

    @parameterized.expand([({}, ['a'], KeyError),
                          ({'a': 1}, ['a', 'b'], KeyError)])
    def test_access_nested_map_exception(self, input_data, path, expected_exception):
        """Test access_nested_map function for exceptions"""
        # Vérifie que la fonction lève l'exception attendue
        self.assertRaises(expected_exception,
                          access_nested_map, input_data, path)

# Classe de test pour la fonction get_json


class TestGetJson(unittest.TestCase):
    """TestGetJson class"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, expected_payload):
        """Test get_json function"""
        # Crée un objet mock de la réponse HTTP
        mock_response = mock.Mock()
        mock_response.json.return_value = expected_payload

        # Utilise patch pour remplacer l'appel à requests.get par un objet mock
        with mock.patch('requests.get', return_value=mock_response):
            # Vérifie que la fonction renvoie le payload attendu
            self.assertEqual(get_json(url), expected_payload)
            # Vérifie que la méthode json de l'objet mock a été appelée exactement une fois
            mock_response.json.assert_called_once()

# Classe de test pour le décorateur memoize


class TestMemoize(unittest.TestCase):
    """TestMemoize class"""

    def test_memoize(self):
        """Test memoize function"""
        # Définit une classe de test pour illustrer l'utilisation de memoize
        class TestClass:
            """TestClass class"""

            def a_method(self):
                """Method that returns 42"""
                return 42

            @memoize
            def a_property(self):
                """Memoized property"""
                return self.a_method()

        # Utilise patch.object pour créer un mock de la méthode a_method dans TestClass
        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            # Crée une instance de TestClass pour le test
            test_instance = TestClass()
            # Accède à la propriété a_property pour la première fois
            returned_value = test_instance.a_property
            # Vérifie que la méthode a_method a été appelée exactement une fois
            self.assertEqual(returned_value, 42)
            mock_method.assert_called_once()


# Point d'entrée pour exécuter les tests lorsque le script est exécuté directement
if __name__ == '__main__':
    unittest.main()
