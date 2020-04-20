import re

from HystrixBox.Decoders.decoder import Decoder

PRINTABLE_ASCII_VALUES = '^(3[2-9]|[4-9][0-9]|1[01][0-9]|12[0-6])$'


class AsciiDecoder(Decoder):
    """
        A class used to represent a ASCII decoder

        :Example:

            ``84 104 105 115 32 105 115 32 97 110 32 101 120 97 109 112 108 101 33 -> This is an example!``

    """

    @staticmethod
    def validate(text):
        return all(bool(re.match(PRINTABLE_ASCII_VALUES, part)) for part in text.split())

    @staticmethod
    def decode(text):
        return [''.join(chr(int(char)) for char in text.split())]
