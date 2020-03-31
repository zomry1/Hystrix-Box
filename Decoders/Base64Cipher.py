import base64


def Base64Decoder(ciphertext):
    return base64.decodebytes(ciphertext)
