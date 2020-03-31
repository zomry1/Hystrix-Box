import requests
import json
import re

APP_ID = "793deab9"
APP_KEY = "adb2496052fe4de3d78bee7bbacf970f"
MISSING_ERROR = 50


def sentenceScore(sentence):
    # Remove Non alphabetic charts
    r2 = re.compile(r'[^a-zA-Z ]', re.MULTILINE)
    sentence = r2.sub('', sentence)
    # All to lower case
    sentence = sentence.lower()
    # print(sentence)
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
    # print(len(sentence))
    # print(len(sentence.split()))

    response = requests.get('https://od-api.oxforddictionaries.com/api/v2/stats/frequency/words/en/', headers=headers,
                            params=params)
    try:
        response = response.json()
    except:
        print(response)

    score = 0
    try:
        for result in response['results']:
            score += result['normalizedFrequency']
    except:
        print(response)
        print(sentence)

    # Reduce missing word by 30: number of words is sentence minus number of return results multiply by missing error
    # print(score)
    score -= (len(sentence.split()) - len(response['results'])) * MISSING_ERROR
    return score


def evaluateSentence(sentence):
    score = 0
    sentence = sentence.split()
    n = 80  # Split for groups of 80 words in group
    parts = [' '.join(sentence[i:i + n]) for i in range(0, len(sentence), n)]
    for part in parts:
        score += sentenceScore(part)
    return score
# Max split 98 words, length of 671
# https://www.wordsapi.com/
# https://wordsapiv1.p.mashape.com/words/sea/frequency
# https://stackoverflow.com/questions/40425033/split-a-string-every-n-words-into-smaller-strings
