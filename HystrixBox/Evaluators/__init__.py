"""
This module include Evaluator abstract class and inheritance class that used to evaluate plaintexts.
Used in Ultimate Decrypter Tool.
"""

from HystrixBox.Evaluators.Evaluator import Evaluator
from HystrixBox.Evaluators.flag_check import FlagEvaluator
from HystrixBox.Evaluators.letter_check import LetterEvaluator
from HystrixBox.Evaluators.word_check import WordEvaluator

__all__ = ['Evaluator', 'FlagEvaluator', 'LetterEvaluator', 'WordEvaluator']
