import logging

###########################
from HystrixBox.Decoders.ascii_cipher import AsciiDecoder
from HystrixBox.Decoders.base64_cipher import Base64Decoder
from HystrixBox.Decoders.caesar_cipher import CaesarDecoder
from HystrixBox.Decoders.hash_cipher import HashDecoder
from HystrixBox.Decoders.morse_cipher import MorseDecoder
from HystrixBox.Decoders.reverse_cipher import ReverseDecoder
###########################
from HystrixBox.parsers import create_decrypter_parser, create_file_parser, create_string_parser, create_zip_extract_parser, \
    create_stego_lsb_parser, create_extractor_parser, DECODERS_MAP, EXTRACTOR_MAP, \
    create_email_analyzer_parser
from HystrixBox.Tools.email_analyzer import email_analyzer
from HystrixBox.Tools.fileType.get_file_extension import get_file_extension
###########################
from HystrixBox.Tools.recursive_decompression import extract_recursive
from HystrixBox.Tools.strings import strings
from HystrixBox.evaluator import evaluate
from HystrixBox.personal_parser import ParserExceptionError

###########################

# Create parser
decrypter_parser = create_decrypter_parser()
file_parser = create_file_parser()
string_parser = create_string_parser()
zip_extract_parser = create_zip_extract_parser()
stego_lsb_parser = create_stego_lsb_parser()
email_analyzer_parser = create_email_analyzer_parser()
extractor_parser = create_extractor_parser()


def basic_module(arguments, parser, func):
    # parse arguments
    try:
        args = parser.parse_args(args=arguments)
    except ParserExceptionError:
        parser.problem = False
        return
    # If there was problem while parsing arguments
    if parser.problem:
        parser.problem = False
        return ''

    if args.verbose:
        logging.basicConfig(level=logging.INFO, format='[INFO] %(message)s')

    # Run module to get result
    result = func(args)

    # Save results to file if correct arguments was given
    if args.output:
        with open(args.output, 'w') as file:
            file.write(result)

    return result


def decrypter_function(args):
    # Get the ciphertext from CLI or file
    if args.ciphertext is not None:
        cipher_txt = args.ciphertext
    else:  # It's a file
        cipher_txt = args.filename.read()

    # If specific decoder set (else use all decoders)
    if args.decoder is not None:
        logging.info('Use specific decoder: ' + args.specific)
        decoder = DECODERS_MAP[args.specific]
        results = decoder(cipher_txt)
        if results == []:
            return 'No result found'

        result = ''
        for i, plaintext in enumerate(results):
            result += '[' + str(i + 1) + '] Result: ' + plaintext + '\n\n'
        return result

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
        functions_string = 'TTT'

    # Try all decoders
    plaintexts = []
    logging.info('Decode ciphertext by Caesar decoder')
    plaintexts += CaesarDecoder.safe_decode(cipher_txt)
    logging.info('Decode ciphertext by ASCII decoder')
    plaintexts += AsciiDecoder.safe_decode(cipher_txt)
    logging.info('Decode ciphertext by Base64 decoder')
    plaintexts += Base64Decoder.safe_decode(cipher_txt)
    logging.info('Decode ciphertext by Reverse decoder')
    plaintexts += ReverseDecoder.safe_decode(cipher_txt)
    logging.info('Decode ciphertext by hash decoder')
    plaintexts += HashDecoder.safe_decode(cipher_txt)
    logging.info('Decode ciphertext by morse decoder')
    plaintexts += MorseDecoder.safe_decode(cipher_txt)

    # Create result string
    result = ''
    evaluatedPlaintexts = evaluate(plaintexts, functions_string, flag_format)[0:args.number]
    for i, plaintext in enumerate(evaluatedPlaintexts):
        result += '[' + str(i + 1) + '] Result: ' + plaintext[0] + '\n\n'

    return result


def decrypter_module(arguments):
    result = basic_module(arguments, decrypter_parser, decrypter_function)
    return result


def file_function(args):
    # Get the file data
    if args.filename is not None:
        return str(get_file_extension(args.filename.name))


def file_module(arguments):
    result = basic_module(arguments, file_parser, file_function)
    return result


def strings_function(args):
    # Get the file data
    if args.filename is not None:
        return strings(args.filename.name, args.n)


def strings_module(arguments):
    result = basic_module(arguments, string_parser, strings_function)
    return result


def zip_extract_function(args):
    # Get the file data
    if args.filename is not None:
        extract_recursive(args.filename.name, args.path)
        return 'Done extracting'


def zip_extract_module(arguments):
    result = basic_module(arguments, zip_extract_parser, zip_extract_function)
    return result


'''
def stegoLSB_function(args):
    # Get the file data
    if args.filename is not None:
        return decode(args.filename.name)


def stegoLSB_module(arguments):
    result = basic_module(arguments, stegoLSBParser, stegoLSB_function)
    return result
'''


def email_analyzer_function(args):
    # Get the file data
    if args.filename is not None:
        results = email_analyzer(args.filename.name)
        return results


def email_analyzer_module(arguments):
    result = basic_module(arguments, email_analyzer_parser, email_analyzer_function)
    return result


def extractor_function(args):
    # Get the file data
    if args.filename is not None:
        data = args.filename.read()

        # If specific extractor set (else use all decoders)
        if args.extractor is not None:
            logging.info('Use specific extractor: ' + args.extractor)
            extractor = EXTRACTOR_MAP[args.extractor]
            result = 'Result:\n'
            str_list = list(list(extractor(data)))
            if not str_list:  # Empty list
                return 'No result found'
            for x in str_list:
                result += (x + '\n')
            return result
        else:  # Not specific extractor set
            result = ''
            for name, extractor in EXTRACTOR_MAP.items():
                result += 'Extract ' + name + ':\n'
                str_list = list(list(extractor(data)))
                if not str_list:
                    result += 'No result found\n'
                for x in str_list:
                    result += (x + '\n')
                result += '\n'
            return result
    return ""  # Should never get here, the argparser should throw  file not found


def extractor_module(arguments):
    result = basic_module(arguments, extractor_parser, extractor_function)
    return result
