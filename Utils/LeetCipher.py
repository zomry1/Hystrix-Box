# Leet Translator V3.1

# This will translate

# Normal english into

# l33t.

# Credit to: baavgai

# Cladus - 15/06/2012


def fromLeet(text):
    leet_dict = (
        ('r', 'are'),
        ('8', 'ate'),
        ('m8', 'mate'),
        ('tht', 'that'),
        ('j00', 'you'),
        ('0', 'o'),
        ('1', 'i'),
        ('3', 'e'),
        ('5', 's'),
        ('4', 'a'),
        ('7', 't'),
    )
    for symbols, replaceStr in leet_dict:
        for symbol in symbols:
            text = text.replace(symbol, replaceStr)
    return text

# message = input("Please enter a message: ")
# print("Translated Message: ", fromLeet(message).lower())
