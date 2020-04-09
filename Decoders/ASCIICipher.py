from Decoders.Decoder import Decoder


class ASCIIDecoder(Decoder):
    @staticmethod
    def validate(text):
        return all(isinstance(part, int) for part in text.split())

    @staticmethod
    def decode(text):
        return ''.join(chr(int(char)) for char in list(text))
