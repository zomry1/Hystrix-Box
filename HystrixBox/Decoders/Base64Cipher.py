import base64
from HystrixBox.Decoders.Decoder import Decoder
import re

BASE64_FORMAT = '^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$'


class Base64Decoder(Decoder):
    """
    A class used to represent a Base64 decoder

    :Example:

        ``VGhpcyBpcyBhbiBleGFtcGxlIQ== -> This is an example!``

    """
    @staticmethod
    def validate(text):
        return bool(re.match(BASE64_FORMAT, text))

    @staticmethod
    def decode(text):
        base64_bytes = text.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        ciphertext = message_bytes.decode('ascii')
        return [ciphertext]
