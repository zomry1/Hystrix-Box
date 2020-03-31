from SanityCheck import evaluation
from WordCheck import evaluateSentence
from FormatCheck import checkFormat,returnFlags
import collections

letterPriority = 1
wordPriority = 1
formatPriority = 2

def evaluate(plaintexts, functionsString, formatString=''):
	#Make plaintext tuple (plaintext, score)
	scoresDictionary  = {plaintext:0 for plaintext in plaintexts}
	
	#Evaluate with letterCheck
	if functionsString[0] == 'T':
		evaluations = []
		#Evaluate each plaintext and calculate error
		for plaintext in plaintexts:
			evaluations.append((plaintext, evaluation(plaintext)))

		#Sort plaintext by error level
		evaluations = sorted(evaluations, key=lambda x: x[1])

		score = len(evaluations)
		for plaintext in evaluations:
			scoresDictionary[plaintext[0]] += (score*letterPriority)
			score -= 1

	#Evaluate with wordCheck
	if functionsString[1] == 'T':
		evaluations = []
		#Evaluate each plaintext and calculate error
		for plaintext in plaintexts:
			evaluations.append((plaintext, evaluateSentence(plaintext)))

		#Sort plaintext by error level
		evaluations = sorted(evaluations, key=lambda x: x[1])

		score = len(evaluations)
		for plaintext in evaluations:
			scoresDictionary[plaintext[0]] += (score*wordPriority)
			score -= 1

	#Evaluate with formatCheck
	if functionsString[2] == 'T' and formatString != '':
		evaluations = []
		#Evaluate each plaintext and calculate error
		for plaintext in plaintexts:
			evaluations.append((plaintext, checkFormat(plaintext,formatString)))

		#Sort plaintext by error level
		evaluations = sorted(evaluations, key=lambda x: x[1])

		score = len(evaluations)
		for plaintext in evaluations:
			scoresDictionary[plaintext[0]] += (score*formatPriority)
			score -= 1

	scoresDictionary = sorted(scoresDictionary.items(), key=lambda x: x[1], reverse=True)		
	return scoresDictionary

