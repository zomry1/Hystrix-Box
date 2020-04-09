from Decoders.Decoder import Decoder


class ReverseDecoder(Decoder):
    @staticmethod
    def validate(text):
        return True

    @staticmethod
    def decode(text):
        return [text[::-1]]