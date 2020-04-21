import logging
from _collections import OrderedDict

from Evaluators.flag_check import FlagEvaluator
from Evaluators.letter_check import LetterEvaluator
from Evaluators.word_check import WordEvaluator

LETTER_PRIORITY = 1000
WORD_PRIORITY = 1000
FORMAT_PRIORITY = 2000


def evaluate_fun(eval_function, plaintexts, scoresDictionary, sortOrder=True):
    evaluations = []
    # Evaluate each plaintext and calculate error
    for plaintext in plaintexts:
        evaluations.append((plaintext, eval_function(plaintext)))

    group_evaluations = {}

    # Group same scores
    for ciphertext, score in evaluations:
        if score in group_evaluations:
            group_evaluations[score].append(ciphertext)
        else:
            group_evaluations[score] = [ciphertext]

    # Sort dictionary
    group_evaluations = OrderedDict(sorted(group_evaluations.items(), reverse=sortOrder))

    # Give the final score based on group position in the dictionary
    score = len(group_evaluations)
    for group in group_evaluations.values():
        for plaintext in group:
            scoresDictionary[plaintext] += (score * FORMAT_PRIORITY)
        score -= 1


def evaluate(plaintexts, functionsString, formatString=''):
    # Make plaintext tuple (plaintext, score)
    scoresDictionary = {plaintext: 0 for plaintext in plaintexts}

    # Evaluate with letterCheck
    if functionsString[0] == 'T':
        logging.info('Evaluate results by letter analysis')
        evaluate_fun(LetterEvaluator.evaluate, plaintexts, scoresDictionary, False)

    # Evaluate with wordCheck
    if functionsString[1] == 'T':
        logging.info('Evaluate results by word analysis')
        # evaluate_fun(WordEvaluator.evaluate, plaintexts, scoresDictionary)

    # Evaluate with formatCheck
    if functionsString[2] == 'T' and formatString != '':
        logging.info('Evaluate results by flag search')
        evaluate_fun(FlagEvaluator.evaluate, [formatString, plaintexts], scoresDictionary)

    logging.info('Sort results')
    scoresDictionary = sorted(scoresDictionary.items(), key=lambda x: x[1], reverse=True)
    return scoresDictionary
