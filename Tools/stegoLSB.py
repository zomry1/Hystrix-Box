from PIL import Image

def string2bits(text):
	return ''.join(format(ord(char), '08b') for char in text)
def bits2string(bits):
	return ''.join([chr(int(bits[i:i + 8],2)) for i in range(0, len(bits), 8)])
'''
def encode(filename, data):
	# Convert data to binary representation
	binary = ''.join(format(ord(c), '08b') for c in data)
	i = 0
	length = len(binary)
	with Image.open(filename) as img:
		width, height = img.size
		for x in range(0, width):
			for y in range(0, height): #Loop over each pixel
				pixel = list(img.getpixel((x,y))) # Get pixel
				for n in range(0,3): # Loop over RGB
					if i > length: # Check if all data already inserted
						break
					pixel[n] = int(binary[i]) #Set the bit to like in the data
					i += 1
				img.putpixel((x,y), tuple(pixel)) #Set the pixel back in the image
		img.save(filename + '_encoded.png', 'PNG')
'''
def encode(filename, data):
	# Convert data to binary representation
	binary = string2bits(data)
	i = 0
	length = len(binary)
	with Image.open(filename) as img:
		width, height = img.size
		for x in range(0, width):
			for y in range(0, height):
				pixel = list(img.getpixel((x, y)))
				for n in range(0, 3):
					if (i < length):
						pixel[n] = int(binary[i])
						i += 1
				img.putpixel((x, y), tuple(pixel))
		img.save(filename + '_encoded.png', 'PNG')


def decode(filename):
	extracted_bin = []
	with Image.open(filename) as img:
		width, height = img.size
		for x in range(0, width):
			for y in range(0, height):
				pixel = list(img.getpixel((x, y)))
				for n in range(0, 3):
					extracted_bin.append(pixel[n])

	data = "".join([str(x) for x in extracted_bin])
	return data



encode('image.png', 'hiomryking')
decode('image.png_encoded.png')