#!/usr/bin/env python3
"""
Main file
"""

import re
from typing import List


def filter_datum(fields, redaction, message, separator) -> str:
    """
    returns the log message obfuscated
    """
    for i in fields:
        message = re.sub(i, redaction, message)
    return message
