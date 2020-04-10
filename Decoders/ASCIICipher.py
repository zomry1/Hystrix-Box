from Decoders.Decoder import Decoder
import re

PRINTABLE_ASCII_VALUES = '^(3[2-9]|[4-9][0-9]|1[01][0-9]|12[0-6])$'


class ASCIIDecoder(Decoder):
    @staticmethod
    def validate(text):
        return all(bool(re.match(PRINTABLE_ASCII_VALUES, part)) for part in text.split())

    @staticmethod
    def decode(text):
        return [''.join(chr(int(char)) for char in text.split())]


