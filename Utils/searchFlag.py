import re


def searchFlag(stringFormat, text):
    stringFormat = stringFormat[:-2]
    regex = stringFormat + '{.*}'
    return re.findall(regex, text, flags=re.IGNORECASE)
