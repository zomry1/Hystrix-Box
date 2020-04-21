import re

from Decoders.decoder import Decoder

T9_FORMAT = r'^(\d)\1*$'
T9_KEYPAD = [" ", ".?!", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]


class T9Decoder(Decoder):
    """
        A class used to represent a T9 decoder, and old phone keypad (numbers to text)

        :Example:

            ``!8 44 444 7777 0 444 7777 0 2 66 0 33 99 2 6 7 555 33 -> This is an example!``

        """

    @staticmethod
    def validate(text):
        return all(bool(re.match(T9_FORMAT, part)) for part in text.split())

    @staticmethod
    def decode(text):
        letters = text.split()
        answer = []
        for j in letters:
            charset = T9_KEYPAD[int(j[0])]
            answer = answer + [charset[(len(j) - 1) % len(charset)]]
        return [''.join(answer)]
