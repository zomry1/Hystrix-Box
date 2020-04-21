import re

from Decoders.decoder import Decoder

# Dictionary representing the morse code chart
# From https://en.wikipedia.org/wiki/Morse_code

SEPARATOR = '/'
MORSE_CODE_DICT = {'.-': 'A', '-...': 'B', '-.-.': 'C',
                   '-..': 'D', '.': 'E', '..-.': 'F',
                   '--.': 'G', '....': 'H', '..': 'I',
                   '.---': 'J', '-.-': 'K', '.-..': 'L',
                   '--': 'M', '-.': 'N', '---': 'O',
                   '.--.': 'P', '--.-': 'Q', '.-.': 'R',
                   '...': 'S', '-': 'T', '..-': 'U',
                   '...-': 'V', '.--': 'W', '-..-': 'X',
                   '-.--': 'Y', '--..': 'Z', '.----': '1',
                   '..---': '2', '...--': '3', '....-': '4',
                   '.....': '5', '-....': '6', '--...': '7',
                   '---..': '8', '----.': '9', '-----': '0',
                   '--..--': ',', '.-.-.-': '.', '..--..': '?',
                   '-..-.': '/', '-....-': '-', '-.--.': '(',
                   '-.--.-': ')', '.----.': "'", '-.-.--': '!',
                   '.-...': '&', '---...': ':', '-.-.-.': ';',
                   '-...-': '=', '.-.-.': '+', '..--.-': '_',
                   '.-..-.': '"', '...-..-': '$', '.--.-.': '@'}


class MorseDecoder(Decoder):
    """
    A class used to represent a Morse decoder

    :Example:

        ``- .... .. ... / .. ... / .- -. / . -..- .- -- .--. .-.. . -.-.-- -> THIS IS AN EXAMPLE!``

    """

    @staticmethod
    def validate(text):
        # Check if there any  codes are in the dictionary
        return any(code in MORSE_CODE_DICT.keys() for code in text.split(' '))

    @staticmethod
    def decode(text):
        plaintexts = []
        # Split by whitespaces but perverse them -> When separators are 3 whitespaces and etc
        text = re.split(r'(\s+)', text)
        text = list(filter(lambda x: x != ' ', text))  # Remove one spaces from list - Those just spaces
        # Foreach optional common separator
        for separator in ['   ', '       ', '/']:
            plaintext = ''
            MORSE_CODE_DICT[separator] = ' '  # Add separator to the dictionary
            plaintexts.append(''.join([MORSE_CODE_DICT.get(code, code) for code in text]))  # Decode
            MORSE_CODE_DICT.pop(separator)  # Clean the dictionary to the next loop
        return plaintexts
