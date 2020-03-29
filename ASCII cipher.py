def ASCIIDecoder(ciphertext):
	return ''.join(chr(int(char)) for char in ciphertext.split())