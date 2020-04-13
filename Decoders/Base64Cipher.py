import base64
from Decoders.Decoder import Decoder
import re

BASE64_FORMAT = '^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$'


class Base64Decoder(Decoder):
    """
    A class used to represent an Base64 decoder
    """
    @staticmethod
    def validate(text):
        """Validate string format for 64Base encoding

        :param text: The cipher-text
        :type text: str

        :returns: Either the text is in the cipher format or not
        :rtype: bool

        """
        return bool(re.match(BASE64_FORMAT, text))

    @staticmethod
    def decode(text):
        """Decode the text by the 64Base encoding

        :param text: The cipher-text
        :type text: str

        :returns: List of the plain-text after decode
        :rtype: list
        """
        base64_bytes = text.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        ciphertext = message_bytes.decode('ascii')
        return [ciphertext]
