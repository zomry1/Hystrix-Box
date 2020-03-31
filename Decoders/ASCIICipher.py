def ASCIIDecoder(ciphertext):
	#If not all the ciphertext is numbers return empty list
    if all(isinstance(part, int) for part in ciphertext.split()):
	    return ''.join(chr(int(char)) for char in list(ciphertext))
    else:
        return []