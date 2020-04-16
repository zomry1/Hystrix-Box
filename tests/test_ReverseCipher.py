from HystrixBox.Decoders.ReverseCipher import ReverseDecoder


def test_validate_true():
    assert (ReverseDecoder.validate('This is a test!_123') == True)


def test_safe_decode():
    assert (ReverseDecoder.safe_decode('This is a test!_123') == ['321_!tset a si sihT'])
