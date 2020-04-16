class Evaluator(object):
    """
    A class used to represent a plaintext Evaluator
    """
    @staticmethod
    def evaluate(self, text):
        """Evaluate plaintext by some parameters

            :param text: The plaintext
            :type text: str

            :returns: Score of the plaintext
            :rtype: int

            :raise NotImplementedError: If the evaluate function not set in the evaluator
            """
        raise NotImplementedError
