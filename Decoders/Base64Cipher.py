import base64
from Utils.base64Validator import checkBase64Format


def Base64Decoder(ciphertext):
    # Check if ciphertext is 64base format
    if not checkBase64Format(ciphertext):
        return []
    try:
        base64_bytes = ciphertext.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        ciphertext = message_bytes.decode('ascii')
        return [ciphertext]
    except:
        return []
