import re


def checkFormat(ciphertext, stringFormat):
    stringFormat = stringFormat[:-2]
    regex = stringFormat + '{.*}'
    flags = re.findall(regex, ciphertext)
    return 1 * len(flags)


def returnFlags(stringFormat, ciphertext):
    stringFormat = stringFormat[:-2]
    regex = stringFormat + '{.*}'
    return re.findall(regex, ciphertext)
