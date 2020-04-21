from Evaluators.evaluator import Evaluator
from Utils.search_flag import searchFlag


class FlagEvaluator(Evaluator):
    """
        A class used to represent a flag evaluator.

        Score based on the occurrences of the flag in the plaintext
    """

    @staticmethod
    def evaluate(text):  # Special case use text as list of format and ciphertext
        return len(searchFlag(text[0], text[1]))
