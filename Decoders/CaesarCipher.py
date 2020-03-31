def CaesarDecode(ciphertext, shift):
    plaintext = ''
    for i in range(len(ciphertext)):  # Foreach char
        char = ciphertext[i]  # Get the char
        if char.isupper():  # Char is uppercase:
            plaintext += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():  # Char is lowercase
            plaintext += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            plaintext += char
    return plaintext


def CaesarDecoder(ciphertext):
    plaintexts = []
    for i in range(26):
        plaintexts.append(CaesarDecode(ciphertext, i + 1))
    return plaintexts
