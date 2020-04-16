from HystrixBox.Evaluators.Evaluator import Evaluator
from HystrixBox.Utils.searchFlag import searchFlag


class FlagEvaluator(Evaluator):
    @staticmethod
    def evaluate(text):  # Special case use text as list of format and ciphertext
        return len(searchFlag(text[0], text[1]))
