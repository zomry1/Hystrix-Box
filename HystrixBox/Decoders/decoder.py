class Decoder(object):
    """
    A class used to represent a Decoder
    """

    @staticmethod
    def validate(text):
        """Validate string format for this cipher.

        :param text: The cipher-text
        :type text: str

        :returns: Either the text is in the cipher format or not
        :rtype: bool

        :raise NotImplementedError: If the validate function not set in the decoder
        """

        raise NotImplementedError

    @staticmethod
    def decode(text):
        """Decode the text by the cipher

        If there are multiple ways to decode the text, return all of them

        :param text: The cipher-text
        :type text: str

        :returns: List of the plain-texts (or plain-text) after decode
        :rtype: list

        :raise NotImplementedError: If the decode function not set in the decoder
        """
        raise NotImplementedError

    @classmethod
    def safe_decode(cls, text):
        """Validate the format of the text and decode it

        First check if the text is in the format of the cipher, if so decode it.
        If the text is not in the format, return empty list

        :param text: The cipher-text
        :type text: str

        :returns: List of the plain-texts (or plain-text) after decode
        :rtype: list
        """

        if cls.validate(text):  # Check the text is in the cipher format
            return cls.decode(text)  # Decode it
        else:
            return []  # The text it's not in the format
