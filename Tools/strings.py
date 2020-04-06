import string
from Utils.searchFlag import searchFlag


def strings(filename, minChars=4):
    results = ''
    with open(filename, errors="ignore") as f:
        result = ""
        for c in f.read():
            if c in string.printable:
                result += c
                continue
            if len(result) >= minChars:
                results +=  result
            result = ""
        if len(result) >= minChars:  # catch result at EOF
            results +=  result
    return ''.join(results)


def stringsFlag(filename, flagFormat, minChars=4):
    flags = []
    for text in strings(filename, minChars):
        flags += searchFlag(flagFormat, text)
    return flags
