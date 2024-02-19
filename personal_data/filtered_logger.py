#!/usr/bin/env python3
"""
0. Regex-ing
(.*?)= value field use motig no gourmand


"""

import re
import logging
from typing import List


""" Task O: """
def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscate sensitive information in a log message.
    """
    # Création d'une expression régulière pour rechercher les champs ds le msg
    # Concaténation des champs avec le séparateur '|'
    pattern = "|".join(fields)
    # Expression régulière complète
    regex = f"({pattern})=(.*?){separator}"
    # Remplacement des occurrences des champs par la valeur de redaction dans le message
    return re.sub(regex, f"\\1={redaction}{separator}", message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    class RedactingFormatter(logging.Formatter):

    def __init__(self, fields: List[str]):
        self.fields = fields
        super().__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """ Format method to filter sensitive values """
        # Filtrer les valeurs sensibles dans le message de journal
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        # Appel de la méthode de formatage de la classe parent pr compléter le formatage
        return super().format(record)


