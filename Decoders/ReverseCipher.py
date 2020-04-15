from Decoders.Decoder import Decoder


class ReverseDecoder(Decoder):
    """
    A class used to represent a Reverse decoder

    :Example:

        ``!elpmaxe na si siht -> This is an example!``

    """
    @staticmethod
    def validate(text):
        return True

    @staticmethod
    def decode(text):
        return [text[::-1]]