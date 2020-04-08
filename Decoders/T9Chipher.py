
def T9Decoder(ciphertext, separator=' '):
	letters = ciphertext.split(separator)
	t9 = [" ",".?!","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
	answer = []
	for j in letters:
		charset = t9[int(j[0])]
		answer = answer + [charset[(len(j)-1) % len(charset)]]
	return ''.join(answer)


# Decode example
# print(T9Decoder('999 666 0 8 44 33 0 333 555 2 4 0 444 7777 0 7777 444 6 7 555 33 0 55 33 999 7 2 3'))
