import requests

EMAIL = 'zyoqrqpytsogftcesk@ttirv.org'
SECRET_CODE = '0a7d25f24a9400cc'


def hashDecoder(ciphertext, hash):
    params = (
        ('hash', ciphertext),
        ('hash_type', hash),
        ('email', 'zyoqrqpytsogftcesk@ttirv.org'),
        ('code', '0a7d25f24a9400cc')
    )

    response = requests.get('https://md5decrypt.net/en/Api/api.php', params=params)
    response = response.content.decode("utf-8")  # Decode answer to string (from bytes)
    if response.startswith("ERROR CODE") or response == '':  # No result
        if response.startswith("ERROR CODE") and response != 'ERROR CODE : 005':  # There is problem with the API
            print('HASH API', response)
        return []
    else:
        return [(response[:-1], hash)]


def hashesDecoder(ciphertext):
    results = []
    hashes = ['md5', 'md4', 'sha1', 'sha256', 'sha384', 'sha512', 'ntlm']
    for hash in hashes:
        results += hashDecoder(ciphertext, hash)
    return results


#print(hashesDecoder('5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'))
