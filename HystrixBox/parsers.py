import argparse

from Decoders.ascii_cipher import AsciiDecoder
from Decoders.base64_cipher import Base64Decoder
from Decoders.caesar_cipher import CaesarDecoder
from Decoders.hash_cipher import HashDecoder
from Decoders.reverse_cipher import ReverseDecoder
############################
from Extractors.email_extractor import EmailExtractor
from Extractors.ip_extractor import IPExtractor
from Extractors.md5_extractor import MD5Extractor
from Extractors.url_extractor import URLExtractor
############################
from personal_parser import MyParser

###########################


ARGS_STR = """
    ___                                                 __       
   /   |   _____ ____ _ __  __ ____ ___   ___   ____   / /_ _____
  / /| |  / ___// __ `// / / // __ `__ \ / _ \ / __ \ / __// ___/
 / ___ | / /   / /_/ // /_/ // / / / / //  __// / / // /_ (__  ) 
/_/  |_|/_/    \__, / \__,_//_/ /_/ /_/ \___//_/ /_/ \__//____/  
              /____/                                             
"""

EPILOGUE_STR = 'Made by zomry1 and Matssu ©'

DECODERS_MAP = {'ascii': AsciiDecoder.safe_decode,
                'base64': Base64Decoder.safe_decode,
                'caesar': CaesarDecoder.safe_decode,
                'reverse': ReverseDecoder.safe_decode,
                'hash': HashDecoder.safe_decode
                }

EXTRACTOR_MAP = {'url': URLExtractor.extract,
                 'ip': IPExtractor.extract,
                 'email': EmailExtractor.extract,
                 'md5': MD5Extractor.extract
                 }


###########################
def create_basic_parser(description):
    # Create argumentParser
    parser = MyParser(
        prog='',
        description='\n' + description + '\n'
                                         'just type the optional arguments that you need from the list\n\n' + ARGS_STR,
        epilog=EPILOGUE_STR,
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.version = '1.0'

    parser.add_argument('filename',
                        type=argparse.FileType('r'))

    # Version flag
    parser.add_argument('--version', action='version')

    # Verbose flag
    parser.add_argument('-v', '--verbose', help='Verbose mode', action='store_true')

    # Output to file
    parser.add_argument('-o', '--output',
                        help='Output file to save the results',
                        metavar='FILENAME')

    return parser


def create_extractor_parser():
    # Create argumentParser
    parser = create_basic_parser('The Ultimate Extractor, Drop your RAW DATA FILE here')
    # Specific extractor flag
    parser.add_argument('-e', '--extractor',
                        help='Choose specific extractor, {%(choices)s}',
                        choices=EXTRACTOR_MAP.keys(),
                        metavar='EXTRACTOR')
    return parser


def create_email_analyzer_parser():
    return create_basic_parser('Analyze email file')


def create_stego_lsb_parser():
    return create_basic_parser('Try to decode data from image by LSB encode')


def create_zip_extract_parser():
    parser = create_basic_parser('Extract recursive zip files')
    # Specific path to extract
    parser.add_argument('-p', '--path',
                        help='Choose path for extract',
                        metavar='PATH')
    return parser


def create_string_parser():
    # Create argumentParser
    parser = create_basic_parser('Finds and prints text strings embedded in binary files such as executables.')
    # Number of results to print
    parser.add_argument('-n',
                        type=int,
                        help='Print sequences of characters that are at least min-len characters long, Default 4',
                        metavar='NUMBER',
                        default=4)
    return parser


def create_file_parser():
    return create_basic_parser('Determine the type of a file')


def create_decrypter_parser():
    parser = MyParser(
        prog='',
        description='\nThe Ultimate Decoder, Drop your Cipher-text here\n'
                    'just type the optional arguments that you need from the list\n\n' + ARGS_STR,
        epilog=EPILOGUE_STR,
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.version = '1.1'

    # Add input flag required (string or filename)
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument('-c', '--ciphertext')
    input_group.add_argument('-f', '--filename', type=argparse.FileType('r'))

    # Version flag
    parser.add_argument('--version', action='version')

    # Specific decoder flag
    parser.add_argument('-d', '--decoder',
                        help='Choose specific decoder, {%(choices)s}',
                        choices=DECODERS_MAP.keys(),
                        metavar='DECODER')

    # Evaluators flags
    parser.add_argument('-cl', '--checkLetter',
                        help='Evaluate results by letter analysis check',
                        action='store_true')

    parser.add_argument('-cw', '--checkWord',
                        help='Evaluate results by word analysis check',
                        action='store_true')

    parser.add_argument('-cf', '--checkFlag',
                        help='Evaluate results by flag format check',
                        metavar='FORMAT')

    # Number of results to print
    parser.add_argument('-n', '--number',
                        type=int,
                        help='Number of results to be printed (sorted by descending score)',
                        metavar='NUMBER',
                        default=1)
    # Verbose flag
    parser.add_argument('-v', '--verbose', help='Verbose mode', action='store_true')

    # Output to file
    parser.add_argument('-o', '--output',
                        help='Output file to save the results',
                        metavar='FILENAME')

    return parser
