from PIL import Image


def string2bits(text):
    return ''.join(format(ord(char), '08b') for char in text)


def bits2string(bits):
    return ''.join([chr(int(bits[i:i + 8], 2)) for i in range(0, len(bits), 8)])


def encode(data, source_image, output_image='encoded_image.png', overwrite_end=True):
    binary = string2bits(data)  # Convert string (ASCII) to string of bits
    i = 0
    length = len(binary)
    with Image.open(source_image) as img:  # Read image
        width, height = img.size
        for x in range(0, width):
            for y in range(0, height):  # Foreach pixel loops
                pixel = list(img.getpixel((x, y)))  # Get pixel
                for n in range(0, 3):  # For each value in RGB
                    if i < length:  # If more data needed to insert in the image
                        pixel[n] = int(binary[i])
                        i += 1
                    elif overwrite_end:  # Overwrite trailing values by zero
                        pixel[n] = 0
                img.putpixel((x, y), tuple(pixel))  # Set the pixel back
        img.save(output_image, 'PNG')  # Save image


def decode(filename):
    extracted_bin = []
    with Image.open(filename) as img:  # Read image
        width, height = img.size
        for x in range(0, width):
            for y in range(0, height):  # For each pixel loops
                pixel = list(img.getpixel((x, y)))  # Get pixel
                for n in range(0, 3):  # For each value in RGB
                    extracted_bin.append(pixel[n] & 1)  # Get value

    data = "".join([str(x) for x in extracted_bin]).rstrip('0')  # Get string of bits and remove trailing zeros
    return bits2string(data)[0:20]


'''
# Run example #
encode('hiomryking', 'image.png')
print(decode('encoded_image.png'))
'''