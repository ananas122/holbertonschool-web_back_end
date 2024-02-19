import re
    """
    Regex 
    """

def filter_datum(fields, redaction, message, separator) -> str:
    """
    returns the log message obfuscated
    """
    return re.sub('|'.join(fields), redaction, message)
