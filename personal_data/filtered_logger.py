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

    def __init__(self, fields: list):
        """ Constructor accepting a list of fields """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Format method to filter sensitive values """
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)


