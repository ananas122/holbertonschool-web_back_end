#!/usr/bin/env python3
"""
0. Regex-ing
"""

import re
from typing import List


def filter_datum(fields, redaction, message, separator) -> str:
    """
    Obfuscate sensitive information in a log message.
    """
    pattern = "|".join(fields)
    regex = f"({pattern})=(.*?){separator}"
    return re.sub(regex, f"\\1={redaction}{separator}", message)
