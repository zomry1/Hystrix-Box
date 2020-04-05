import logging
###########################
from Decoders.ASCIICipher import ASCIIDecoder
from Decoders.Base64Cipher import Base64Decoder
from Decoders.CaesarCipher import CaesarDecoder
from Decoders.ReverseCipher import ReverseDecoder
###########################
from Extractors.emailExtractor import extractEmail
from Extractors.ipExtractor import extractIP
from Extractors.urlExtractor import extractUrl
###########################
from personal_parser import MyParser, ParserException
from evaluator import evaluate
###########################
import argparse

###########################

ARGS_STR = """
    ___                                                 __       
   /   |   _____ ____ _ __  __ ____ ___   ___   ____   / /_ _____
  / /| |  / ___// __ `// / / // __ `__ \ / _ \ / __ \ / __// ___/
 / ___ | / /   / /_/ // /_/ // / / / / //  __// / / // /_ (__  ) 
/_/  |_|/_/    \__, / \__,_//_/ /_/ /_/ \___//_/ /_/ \__//____/  
              /____/                                             
"""

DECODERS_MAP = {'ascii': ASCIIDecoder,
                'base64': Base64Decoder,
                'caesar': CaesarDecoder,
                'reverse': ReverseDecoder}

EXTRACTOR_MAP = {'url': extractUrl,
                 'ip': extractIP,
                 'email': extractEmail}


###########################

def decrypter_module(arguments):
    # Create argumentParser
    parser = MyParser(
        description='\nThe Ultimate Decoder, Drop your Cipher-text here\n'
                    'just type the optional arguments that you need from the list\n\n' + ARGS_STR,
        epilog='Just boring epilogue',
        formatter_class=argparse.RawTextHelpFormatter,
        add_help=False
    )

    parser.version = '1.1'

    # Add input flag required (string or filename)
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument('-c', '--ciphertext')
    input_group.add_argument('-f', '--filename', type=argparse.FileType('r'))
    # Help flag
    input_group.add_argument('-h', '--help', action='help')
    # Version flag
    parser.add_argument('--version', action='version')

    # Specific decoder flag
    parser.add_argument('-s', '--specific',
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
    parser.add_argument('-n',
                        type=int,
                        help='Number of results to be printed (sorted by descending score',
                        metavar='NUMBER',
                        default=1)
    # Verbose flag
    parser.add_argument('-v', '--verbose', help='Verbose mode', action='store_true')

    # Output to file
    parser.add_argument('-o', '--output',
                        help='Output file to save the results',
                        metavar='FILENAME')

    # parse arguments
    try:
        args = parser.parse_args(args=arguments)
    except ParserException:
        return
    # If there was problem while parsing arguments
    if parser.problem:
        return ''

    if args.verbose:
        logging.basicConfig(level=logging.INFO, format='[INFO] %(message)s')

    # Get the ciphertext from CLI or file
    if args.ciphertext is not None:
        cipher_txt = args.ciphertext
    else:  # It's a file
        cipher_txt = args.filename.read()

    # If specific decoder set (else use all decoders)
    if args.specific is not None:
        logging.info('Use specific decoder: ' + args.specific)
        decoder = DECODERS_MAP[args.specific]
        return decoder(cipher_txt)

    # If specific evaluator set (else use all evaluators)
    functions_string = ['F', 'F', 'F']
    flag_format = ''
    if args.checkLetter or args.checkWord or args.checkFlag:
        if args.checkLetter:
            functions_string[0] = 'T'
            logging.info('Add specific evaluator: letter analysis')
        if args.checkWord:
            functions_string[1] = 'T'
            logging.info('Add specific evaluator: word analysis')
        if args.checkFlag:
            functions_string[2] = 'T'
            logging.info('Add specific evaluator: flag search')
            flag_format = args.checkFlag
        functions_string = ''.join(functions_string)
    else:
        logging.info('Use all evaluators')
        functions_string = 'TFT'  ##############Change this to TTT!!!!!!!!!!!!

    # Try all decoders
    plaintexts = []
    logging.info('Decode ciphertext by Caesar decoder')
    plaintexts += CaesarDecoder(cipher_txt)
    logging.info('Decode ciphertext by ASCII decoder')
    plaintexts += ASCIIDecoder(cipher_txt)
    logging.info('Decode ciphertext by Base64 decoder')
    plaintexts += Base64Decoder(cipher_txt)
    logging.info('Decode ciphertext by Reverse decoder')
    plaintexts += ReverseDecoder(cipher_txt)

    # Create result string
    result = ''
    evaluatedPlaintexts = evaluate(plaintexts, functions_string, flag_format)[0:args.n]
    for i, plaintext in enumerate(evaluatedPlaintexts):
        result += '[' + str(i + 1) + '] Result: ' + plaintext[0] + '\n\n'

    # Save results to file if correct arguments was given
    if args.output:
        with open(args.output, 'w') as file:
            file.write(result)

    return result



def forensics_module(arguments):
    pass  # TODO


def extractor_module(arguments):
    # Create argumentParser
    parser = MyParser(
        description='\nThe Ultimate Extractor, Drop your RAW DATA FILE here\n'
                    'just type the optional arguments that you need from the list\n\n' + ARGS_STR,
        epilog='Just boring epilogue',
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.version = '1.1'


    parser.add_argument('filename',
                        type=argparse.FileType('r'))

    # Version flag
    parser.add_argument('--version', action='version')

    # Specific decoder flag
    parser.add_argument('extractor',
                        help='Choose specific extractor, {%(choices)s}',
                        choices=EXTRACTOR_MAP.keys(),
                        metavar='EXTRACTOR')

    # # Verbose flag
    #     # parser.add_argument('-v', '--verbose', help='Verbose mode', action='store_true')

    # parse arguments
    args = parser.parse_args(args=arguments)
    # If there was problem while parsing arguments
    if parser.problem:
        return ''

    # if args.verbose:
    #     logging.basicConfig(level=logging.INFO, format='[INFO] %(message)s')

    # Get the file data
    if args.filename is not None:
        data = args.filename.read()
        # Extractor part
        # logging.info('Used Extractor: ' + args.specific)
        extractor = EXTRACTOR_MAP[args.extractor]
        result = 'Result:\n'
        str_list = list(list(extractor(data)))
        # special case
        if args.extractor == 'url':
            for x in str_list:
                result += (x[0] + '\n')
        else:
            for x in str_list:
                result += (x + '\n')
        return result
    # not sure about this
    return ""
