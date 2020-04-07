english_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']


def GematriaDecoder(ciphertext, separator=' '):
    result = ''
    numbers = ciphertext.split(separator)
    for number in numbers:
        if number.isdigit():
            result += english_letters[int(number)-1]
        else:
            result += number
    return [result]


#print(GematriaDecoder('16 9 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }'))
