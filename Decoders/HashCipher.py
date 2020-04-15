import requests
import re
from Decoders.Decoder import Decoder
# Disable warnings
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# https://www.nitrxgen.net/md5db_info/#api
'''
HASH_FORMAT = '^(?:[a-fA-F\d]{32,40})$' \
              '|^(?:[a-fA-F\d]{52,60})$' \
              '|^(?:[a-fA-F\d]{92,100})$' \
              '|^(?:[A-Fa-f0-9]{64})$' \
              '|^(?:[A-Fa-f0-9]{128})$'
'''
MD5_FORMAT = r'([a-fA-F\d]{32})'


class HashDecoder(Decoder):
    """
    A class used to represent a Hash decoder

    .. note:: correctly support only md5 hash
            using www.nitrxgen.net API

    :Example:

        ``a85a7dae016693c9351110c357e4b609 -> This is an example!``

    """
    @staticmethod
    def validate(text):
        return bool(re.match(MD5_FORMAT, text))

    @staticmethod
    def decode(text):
        try:
            response = requests.get('https://www.nitrxgen.net/md5db/' + text, verify=False).text
            if response:
                return [response]
            else:
                return []
        except:
            return []
