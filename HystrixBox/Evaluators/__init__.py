"""
This module include Evaluator abstract class and inheritance class that used to evaluate plaintexts.
Used in Ultimate Decrypter Tool.
"""

from Evaluators.evaluator import Evaluator
from Evaluators.flag_check import FlagEvaluator
from Evaluators.letter_check import LetterEvaluator
from Evaluators.word_check import WordEvaluator

__all__ = ['Evaluator', 'FlagEvaluator', 'LetterEvaluator', 'WordEvaluator']
