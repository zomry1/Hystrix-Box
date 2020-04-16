import requests
import re

from HystrixBox.Evaluators.Evaluator import Evaluator
from HystrixBox.passwords import APP_ID, APP_KEY

MISSING_ERROR = 50


# https://www.wordsapi.com/
# https://wordsapiv1.p.mashape.com/words/sea/frequency
# https://stackoverflow.com/questions/40425033/split-a-string-every-n-words-into-smaller-strings


def sentenceScore(sentence):
    # Remove Non alphabetic charts
    r2 = re.compile(r'[^a-zA-Z ]', re.MULTILINE)
    sentence = r2.sub('', sentence)
    # All to lower case
    sentence = sentence.lower()
    score = 0
    headers = {
        'Accept': 'application/json',
        'APP_ID': APP_ID,
        'APP_KEY': APP_KEY,
    }

    params = (
        ('corpus', 'nmc'),
        ('trueCases', sentence.split()),
        ('collate', 'trueCase')
    )

    response = requests.get('https://od-api.oxforddictionaries.com/api/v2/stats/frequency/words/en/', headers=headers,
                            params=params)
    try:
        response = response.json()
    except:
        print(response)

    try:
        for result in response['results']:
            score += result['normalizedFrequency']
    except:
        print(response)
        print(sentence)

    # Reduce missing word by 30: number of words is sentence minus number of return results multiply by missing error
    score -= (len(sentence.split()) - len(response['results'])) * MISSING_ERROR
    return score


class WordEvaluator(Evaluator):
    @staticmethod
    def evaluate(text):
        score = 0
        sentence = text.split()
        n = 80  # Split for groups of 80 words in group
        parts = [' '.join(sentence[i:i + n]) for i in range(0, len(sentence), n)]
        for part in parts:
            score += sentenceScore(part)
        return score
