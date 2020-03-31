from Checkers.letter_check import evaluation
from Checkers.word_check import evaluateSentence
from Checkers.flag_check import checkFormat
from _collections import OrderedDict

LETTER_PRIORITY = 1000
WORD_PRIORITY = 1000
FORMAT_PRIORITY = 2000


def evaluate_fun(eval_function, plaintexts, scoresDictionary, sortOrder=True, formatString=''):
    evaluations = []
    # Check if formatString is needed to be sent
    if formatString != '':
        # Evaluate each plaintext and calculate error
        for plaintext in plaintexts:
            evaluations.append((plaintext, eval_function(plaintext, formatString)))
    else:
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
        evaluate_fun(evaluation, plaintexts, scoresDictionary, False)
        #############################################################
        '''
        evaluations = []
        # Evaluate each plaintext and calculate error
        for plaintext in plaintexts:
            evaluations.append((plaintext, evaluation(plaintext)))

        # Sort plaintext by error level
        evaluations = sorted(evaluations, key=lambda x: x[1])

        score = len(evaluations)
        for plaintext in evaluations:
            scoresDictionary[plaintext[0]] += (score * LETTER_PRIORITY)
            score -= 1
        '''

    # Evaluate with wordCheck
    if functionsString[1] == 'T':
        evaluate_fun(evaluateSentence, plaintexts, scoresDictionary)
        '''
        evaluations = []
        # Evaluate each plaintext and calculate error
        for plaintext in plaintexts:
            evaluations.append((plaintext, evaluateSentence(plaintext)))

        # Sort plaintext by error level
        evaluations = sorted(evaluations, key=lambda x: x[1], reverse=True)

        score = len(evaluations)
        for plaintext in evaluations:
            scoresDictionary[plaintext[0]] += (score * WORD_PRIORITY)
            score -= 1
        '''

    # Evaluate with formatCheck
    if functionsString[2] == 'T' and formatString != '':
        evaluate_fun(checkFormat, plaintexts, scoresDictionary, formatString=formatString)
        '''
        evaluations = []
        # Evaluate each plaintext and calculate error
        for plaintext in plaintexts:
            evaluations.append((plaintext, checkFormat(formatString, plaintext)))

        # Sort plaintext by error level
        # evaluations = sorted(evaluations, key=lambda x: x[1], reverse=True)
        group_evaluations = {}

        for ciphertext, score in evaluations:
            if score in group_evaluations:
                group_evaluations[score].append(ciphertext)
            else:
                group_evaluations[score] = [ciphertext]

        score = len(group_evaluations)
        # Need to be sorted
        for group in group_evaluations.values():
            for plaintext in group:
                scoresDictionary[plaintext] += (score * FORMAT_PRIORITY)
            score -= 1
        '''

    scoresDictionary = sorted(scoresDictionary.items(), key=lambda x: x[1], reverse=True)
    return scoresDictionary
