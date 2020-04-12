from Decoders.T9Chipher import T9Decoder


def test_validate_true():
    assert (T9Decoder.validate(
        '999 666 0 8 44 33 0 333 555 2 4 0 444 7777 0 7777 444 6 7 555 33 0 55 33 999 7 2 3') == True)


def test_validate_false_not_repeating_numbers():
    assert (T9Decoder.validate(
        '9199 6636 0 8 44 33 01 333 555 2 4 0 444 7777 0 7777 444 6 7 555 33 0 55 33 999 7 2 3') == False)


def test_validate_false_not_only_numbers():
    assert (T9Decoder.validate(
        '999 66a6 0 8 4i4 33 0 3c33 555 2 4 0 444 7777 0 7777 444 6 7 555 33 0 55 33 999 7 2 3') == False)


def test_safe_decode_true():
    assert (T9Decoder.safe_decode('999 666 0 8 44 33 0 333 555 2 4 0 444 7777 0 7777 444 6 7 555 33 0 55 33 999 7 2 3')
            == ['YO THE FLAG IS SIMPLE KEYPAD'])


def test_safe_decode_false():
    assert (T9Decoder.safe_decode('999 66a6 0 8 4i4 33 0 3c33 555 2 4 0 444 7777 0 7777 444 6 7 555 33 0 55 33 999 7 '
                                  '2 3') == [])
