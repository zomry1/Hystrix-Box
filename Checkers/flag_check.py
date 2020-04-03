from Utils.searchFlag import searchFlag


def checkFormat(ciphertext, stringFormat):
    return len(searchFlag(stringFormat, ciphertext))
