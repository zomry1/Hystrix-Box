import re

import requests

from HystrixBox.Evaluators.evaluator import Evaluator
from HystrixBox.keys import APP_ID, APP_KEY

MISSING_ERROR = 50


# https://developer.oxforddictionaries.com/


def sentence_score(sentence):
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
        print(response.status_code)
        return -1

    for result in response['results']:
        score += result['normalizedFrequency']

    # Reduce missing word by 30: number of words is sentence minus number of return results multiply by missing error
    score -= (len(sentence.split()) - len(response['results'])) * MISSING_ERROR
    return score


class WordEvaluator(Evaluator):
    """
        A class used to represent a letter analysis evaluator.

        Score based on checking words in the english words frequencies, implement by www.wordsapi.com
    """

    @staticmethod
    def evaluate(text):
        score = 0
        sentence = text.split()
        n = 80  # Split for groups of 80 words in group
        parts = [' '.join(sentence[i:i + n]) for i in range(0, len(sentence), n)]
        for part in parts:
            score += sentence_score(part)
        return score
