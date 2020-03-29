import re
from collections import Counter


english_frequency = {'e':12.02, 't':9.1, 'a':8.12, 'o':7.68, 'i':7.31, 'n':6.95, 's':6.28, 'r':6.02, 'h':5.92, 'd':4.32, 'l':3.98, 'u':2.88,
'c':2.71, 'm':2.61, 'f':2.30, 'y':2.11, 'w':2.09, 'g':2.03, 'p':1.82, 'b':1.49, 'v':1.11, 'k':0.69, 'x':0.17, 'q':0.11, 'j':0.10, 'z':0.07}

def Frequency_Analysis(chipertext):
	#Remove Non alphabetic charts
	r2 = re.compile(r'[^a-zA-Z]', re.MULTILINE)
	chipertext = r2.sub('', chipertext)
	#All to lower case
	chipertext = chipertext.lower()

	#Get frequencies
	frequencies = Counter(chipertext).most_common()
	#Make frequencies to percentages
	percentages = [(letter, count / len(chipertext) * 100) for letter, count in frequencies]
	return percentages


def getChi2(percentages):
	error = 0
	for observetion in percentages:
		letter = observetion[0]
		obs = observetion[1]
		exp = english_frequency[letter]
		error += (pow((obs-exp),2)/exp)
	return error

def evaluation(chipertext):
	percentages = Frequency_Analysis(chipertext)
	error = getChi2(percentages)
	return error

#https://crypto.stackexchange.com/questions/30209/developing-algorithm-for-detecting-plain-text-via-frequency-analysis
#https://www.wordsapi.com/
#https://wordsapiv1.p.mashape.com/words/sea/frequency