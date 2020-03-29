import re
from collections import Counter


english = {'e':12.02, 't':9.1, 'a':8.12, 'o':7.68, 'i':7.31, 'n':6.95, 's':6.28, 'r':6.02, 'h':5.92, 'd':4.32, 'l':3.98, 'u':2.88,
'c':2.71, 'm':2.61, 'f':2.30, 'y':2.11, 'w':2.09, 'g':2.03, 'p':1.82, 'b':1.49, 'v':1.11, 'k':0.69, 'x':0.17, 'q':0.11, 'j':0.10, 'z':0.07}
def Frequency_Analysis(chipertext):
	#Remove Non alpahbetic charts
	r2 = re.compile(r'[^a-zA-Z]', re.MULTILINE)
	chipertext = r2.sub('', chipertext)
	#All to lower case
	chipertext = chipertext.lower()

	#Get frequncies
	frequencies = Counter(chipertext).most_common()
	#Make frequncies to precentages
	percentages = [(letter, count / len(chipertext) * 100) for letter, count in frequencies]
	return percentages
	#print(percentages)

def getChi2(percentages):
	error = 0
	for observetion in percentages:
		letter = observetion[0]
		obs = observetion[1]
		exp = english[letter]
		error += (pow((obs-exp),2)/exp)
	return error

def Decoder(chipertext):
	percentages = Frequency_Analysis(chipertext)
	error = getChi2(percentages)
	print(error)

text = """Perhaps the most well-publicized tech tool in Russia's arsenal for fighting coronavirus is Moscow's massive facial-recognition system. Rolled out earlier this year, the surveillance system had originally prompted an unusual public backlash, with privacy advocates filing lawsuits over unlawful surveillance.
Coronavirus, however, has given an unexpected public-relations boost to the system.
Last week, Moscow police claimed to have caught and fined 200 people who violated quarantine and self-isolation using facial recognition and a 170,000-camera system. According to a Russian media report some of the alleged violators who were fined had been outside for less than half a minute before they were picked up by a camera.
"We want there to be even more cameras so that that there is no dark corner or side street left," Oleg Baranov, Moscow's police chief, said in a recent briefing, adding that the service is currently working to install an additional 9,000 cameras."""

text1 = """dsadsadsadasdsadasdasdasdasdsadsadasdasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasasas
lice chief, sdsaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaall an additional 9,000 cameras."""

Decoder(text1)


#https://crypto.stackexchange.com/questions/30209/developing-algorithm-for-detecting-plain-text-via-frequency-analysis
#https://www.wordsapi.com/
#https://wordsapiv1.p.mashape.com/words/sea/frequency