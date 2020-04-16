from HystrixBox.Decoders.Decoder import Decoder


def CaesarDecode(ciphertext, shift):
    plaintext = ''
    for i in range(len(ciphertext)):  # Foreach char
        char = ciphertext[i]  # Get the char
        if char.isupper():  # Char is uppercase:
            plaintext += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():  # Char is lowercase
            plaintext += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            plaintext += char
    return plaintext


class CaesarDecoder(Decoder):
    """
    A class used to represent a Caesar decoder

    .. note:: brute-force all options (shifts) and return list of all possible options
            starting from 1-shift to 25-shift

    :Example:

        ``Rfgq gq yl cvyknjc! -> [Sghr hr zm dwzlokd!, This is an example!, Uijt jt bo fybnqmf!] and go on``

    """
    @staticmethod
    def validate(text):
        return True

    @staticmethod
    def decode(text):
        plaintexts = []
        for i in range(25):
            plaintexts.append(CaesarDecode(text, i + 1))
        return plaintexts
