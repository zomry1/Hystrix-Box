import re
from collections import Counter

def Frequency_Analysis(plaintext):
	#Remove Non alpahbetic charts
	r2 = re.compile(r'[^a-zA-Z0-9]', re.MULTILINE)
	plaintext = r2.sub('', plaintext)
	#All to lower case
	plaintext = plaintext.lower()

	#Get frequncies
	frequencies = Counter(plaintext).most_common()
	#Make frequncies to precentages
	percentages = [(letter, count / len(plaintext) * 100) for letter, count in frequencies]
	print(percentages)

text = """Perhaps the most well-publicized tech tool in Russia's arsenal for fighting coronavirus is Moscow's massive facial-recognition system. Rolled out earlier this year, the surveillance system had originally prompted an unusual public backlash, with privacy advocates filing lawsuits over unlawful surveillance.
Coronavirus, however, has given an unexpected public-relations boost to the system.
Last week, Moscow police claimed to have caught and fined 200 people who violated quarantine and self-isolation using facial recognition and a 170,000-camera system. According to a Russian media report some of the alleged violators who were fined had been outside for less than half a minute before they were picked up by a camera.
"We want there to be even more cameras so that that there is no dark corner or side street left," Oleg Baranov, Moscow's police chief, said in a recent briefing, adding that the service is currently working to install an additional 9,000 cameras."""

Frequency_Analysis(text)



#https://www.wordsapi.com/
#https://wordsapiv1.p.mashape.com/words/sea/frequency