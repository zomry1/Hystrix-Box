import base64
from Decoders.Decoder import Decoder
import re

BASE64_FORMAT = '^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$'


class Base64Decoder(Decoder):
    @staticmethod
    def validate(text):
        return bool(re.match(BASE64_FORMAT, text))

    @staticmethod
    def decode(text):
        try:
            base64_bytes = text.encode('ascii')
            message_bytes = base64.b64decode(base64_bytes)
            ciphertext = message_bytes.decode('ascii')
            return [ciphertext]
        except:
            return []
