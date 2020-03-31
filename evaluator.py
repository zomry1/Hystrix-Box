from Checkers.letter_check import evaluation
from Checkers.word_check import evaluateSentence
from Checkers.flag_check import checkFormat

LETTER_PRIORITY = 1000
WORD_PRIORITY = 1000
FORMAT_PRIORITY = 2000


def evaluate(plaintexts, functionsString, formatString=''):
    # Make plaintext tuple (plaintext, score)
    scoresDictionary = {plaintext: 0 for plaintext in plaintexts}

    # Evaluate with letterCheck
    if functionsString[0] == 'T':
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

    # Evaluate with wordCheck
    if functionsString[1] == 'T':
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

    # Evaluate with formatCheck
    if functionsString[2] == 'T' and formatString != '':
        evaluations = []
        # Evaluate each plaintext and calculate error
        for plaintext in plaintexts:
            evaluations.append((plaintext, checkFormat(formatString, plaintext)))

        # Sort plaintext by error level
        evaluations = sorted(evaluations, key=lambda x: x[1], reverse=True)

        score = len(evaluations)
        for plaintext in evaluations:
            scoresDictionary[plaintext[0]] += (score * FORMAT_PRIORITY)
            score -= 1

    scoresDictionary = sorted(scoresDictionary.items(), key=lambda x: x[1], reverse=True)
    return scoresDictionary
