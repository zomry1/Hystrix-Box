import re


def searchFlag(string_format, text):
    string_format = string_format[:-2]
    regex = string_format + '{.*}'
    return re.findall(regex, text, flags=re.IGNORECASE)
