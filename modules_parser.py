import logging
###########################
from Decoders.ASCIICipher import ASCIIDecoder
from Decoders.Base64Cipher import Base64Decoder
from Decoders.CaesarCipher import CaesarDecoder
from Decoders.HashCipher import hashesDecoder
from Decoders.ReverseCipher import ReverseDecoder
###########################
from Extractors.emailExtractor import extractEmail
from Extractors.ipExtractor import extractIP
from Extractors.md5Extractor import extractMD5
from Extractors.urlExtractor import extractUrl
###########################
from Parsers import createDecrypterParser, createFileParser, createStringParser, createZipExtractParser, \
    createStegoLSBParser, createExtractorParser, DECODERS_MAP, EXTRACTOR_MAP, \
    createEmailAnalyzerParser
from Tools.emailAnalyzer import email_analyzer
from Tools.file.getFileExtenstion import getFileExtension
###########################
from Tools.recursiveDecompression import extract_recursive
from Tools.stegoLSB import decode
from Tools.strings import strings
from personal_parser import MyParser, ParserException
from evaluator import evaluate

###########################

# Create parser
decrypterParser = createDecrypterParser()
fileParser = createFileParser()
stringParser = createStringParser
zipExtractParser = createZipExtractParser()
stegoLSBParser = createStegoLSBParser()
emailAnalyzerParser = createEmailAnalyzerParser()
extractorParser = createExtractorParser()


def basic_module(arguments, parser, func):
    # parse arguments
    try:
        args = parser.parse_args(args=arguments)
    except ParserException:
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
    if args.specific is not None:
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
    logging.info('Decode ciphertext by hash decoder')
    plaintexts += hashesDecoder(cipher_txt)

    # Create result string
    result = ''
    evaluatedPlaintexts = evaluate(plaintexts, functions_string, flag_format)[0:args.n]
    for i, plaintext in enumerate(evaluatedPlaintexts):
        result += '[' + str(i + 1) + '] Result: ' + plaintext[0] + '\n\n'

    return result


def decrypter_module(arguments):
    result = basic_module(arguments, decrypterParser, decrypter_function)
    return result


def file_function(args):
    # Get the file data
    if args.filename is not None:
        return str(getFileExtension(args.filename.name))


def file_module(arguments):
    result = basic_module(arguments, fileParser, file_function)
    return result


def strings_function(args):
    # Get the file data
    if args.filename is not None:
        return strings(args.filename.name, args.n)


def strings_module(arguments):
    result = basic_module(arguments, stringParser, strings_function)
    return result


def zip_extract_function(args):
    # Get the file data
    if args.filename is not None:
        extract_recursive(args.filename.name, args.output)
        return 'Done extracting'


def zip_extract_module(arguments):
    result = basic_module(arguments, zipExtractParser, zip_extract_function)
    return result


def stegoLSB_function(args):
    # Get the file data
    if args.filename is not None:
        return decode(args.filename.name)


def stegoLSB_module(arguments):
    result = basic_module(arguments, stegoLSBParser, stegoLSB_function)
    return result


def emailAnalyzer_function(args):
    # Get the file data
    if args.filename is not None:
        results = email_analyzer(args.filename.name)
        print(results)


def emailAnalyzer_module(arguments):
    result = basic_module(arguments, emailAnalyzerParser, emailAnalyzer_function)
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
            if str_list == []:
                return 'No result found'
            for x in str_list:
                    result += (x + '\n')
            return result
        else: #Not specific extractor set
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
    return "" # Should never get here, the argparser should throw  file not found


def extractor_module(arguments):
    result = basic_module(arguments, extractorParser, extractor_function)
    return result


def forensics_module(arguments):
    pass  # TODO