import base64


def Base64Decoder(ciphertext):
    try:
        base64_bytes = ciphertext.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        ciphertext = message_bytes.decode('ascii')
        return [ciphertext]
    except:
        return []
