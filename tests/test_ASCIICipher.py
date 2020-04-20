from HystrixBox.Decoders.ascii_cipher import AsciiDecoder


def test_validate_true():
    assert (AsciiDecoder.validate('84 104 105 115 32 105 115 32 97 32 84 101 115 116 33') == True)


def test_validate_false_not_printable_value():
    assert (AsciiDecoder.validate('1 104 105 115 32 105 115 32 97 32 84 101 115 116 33') == False)


def test_validate_false():
    assert (AsciiDecoder.validate('84d104s300 115 32 105 115 32 97 32 84 101 115 116 33') == False)


def test_safe_decode_true():
    assert (AsciiDecoder.safe_decode('84 104 105 115 32 105 115 32 97 32 84 101 115 116 33') == ['This is a Test!'])


def test_safe_decode_not_printable_ascii():
    assert (AsciiDecoder.safe_decode('1 104 105 115 32 105 115 32 97 32 84 101 115 116 33') == [])


def test_safe_decode_not_numbers():
    assert (AsciiDecoder.safe_decode('1 2sad 1!5 115 32 1$5 115 32 97 32 84 101 115 116 33') == [])
