from Decoders.Decoder import Decoder
import re

T9_FORMAT = r'^(\d)\1*$'
T9_KEYPAD = [" ", ".?!", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]


class T9Decoder(Decoder):
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
