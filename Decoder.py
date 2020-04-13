class Decoder(object):
    """
    A class used to represent an Decoder

    ...

    Methods
    ----------
    validate : bool
        Validate string format for this cipher
    decode : list
        Decode the text by this cipher
    safe_decode : list
        Check the string format by validate and decode it
    """
    @staticmethod
    def validate(text):
        """Validate string format for this cipher.

        :param text: The cipher-text
        :type text: str

        re


        Raises
        -------
        NotImplementedError
            If no format set for this decoder
        """

        raise NotImplementedError

    @staticmethod
    def decode(text):
        raise NotImplementedError

    @classmethod
    def safe_decode(cls, text):
        if cls.validate(text):  # Check the text is in the cipher format
            return cls.decode(text)  # Decode it
        else:
            return []  # The text it's not in the format
