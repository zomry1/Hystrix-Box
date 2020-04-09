import requests
import re
from Decoders.Decoder import Decoder
from passwords import EMAIL, SECRET_CODE

HASH_FORMAT = '^(?:[a-fA-F\d]{32,40})$|^(?:[a-fA-F\d]{52,60})$|^(?:[a-fA-F\d]{92,100})$'


def hashDecoder(ciphertext, hash):
    params = (
        ('hash', ciphertext),
        ('hash_type', hash),
        ('email', EMAIL),
        ('code', SECRET_CODE)
    )

    response = requests.get('https://md5decrypt.net/en/Api/api.php', params=params)
    response = response.content.decode("utf-8")  # Decode answer to string (from bytes)
    if response.startswith("ERROR CODE") or response == '':  # No result
        if response.startswith("ERROR CODE") and response != 'ERROR CODE : 005':  # There is problem with the API
            print('HASH API', response)
        return []
    else:
        return [response[:-1]]


class HashDecoder(Decoder):
    @staticmethod
    def validate(text):
        return bool(re.match(HASH_FORMAT, text))

    @staticmethod
    def decode(text):
        results = []
        hashes = ['md5', 'md4', 'sha1', 'sha256', 'sha384', 'sha512', 'ntlm']
        for hash in hashes:
            results += hashDecoder(text, hash)
        return results

# Decode example
# print(hashesDecoder('5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'))
