from HystrixBox.Decoders.HashCipher import HashDecoder


def test_validate_md5_true():
    assert (HashDecoder.validate('89742a09d9b41329b850b76a76b05e00') == True)


def test_validate_md5_short():
    assert (HashDecoder.validate('89742a09d9b41325e00') == False)


def test_validate_md5_long():
    assert (HashDecoder.validate('89742a09d9bdsds343sad3gfdf32df232f23f41325e00') == False)


def test_validate_md5_symbol():
    assert (HashDecoder.validate('89742a09d9b41@%!b850b76a76b05e00') == False)


def test_safe_decode_md5(socket_enabled):
    assert (HashDecoder.safe_decode('89742a09d9b41329b850b76a76b05e00') == ['this is a test!'])


def test_safe_decode_md5_no_internet():
    assert (HashDecoder.safe_decode('89742a09d9b41329b850b76a76b05e00') == [])


def test_safe_decode_hashNotFound(socket_enabled):
    assert (HashDecoder.safe_decode('5881a59960288f1e07ae73e1882dfdbe') == [])
