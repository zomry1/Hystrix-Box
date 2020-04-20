from HystrixBox.Decoders.base64_cipher import Base64Decoder


def test_validate_true():
    assert (Base64Decoder.validate('dGhpcyBpcyBhIHRlc3Q=') == True)


def test_validate_false():
    assert (Base64Decoder.validate('dGhpcyBpcyBhIHRlc3Q==') == False)


def test_safe_decode_true():
    assert (Base64Decoder.safe_decode('dGhpcyBpcyBhIHRlc3Q=') == ['this is a test'])


def test_safe_decode_noFormat():
    assert (Base64Decoder.safe_decode('dGhpcyBpcyBhIHRlc3Q==') == [])
