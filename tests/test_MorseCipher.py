from HystrixBox.Decoders.MorseCipher import MorseDecoder

TEST4 = ['THIS/IS/AN/EXAMPLE!', 'THIS/IS/AN/EXAMPLE!', 'THIS IS AN EXAMPLE!']


def test_validate_true_with_slash():
    assert (MorseDecoder.validate('- .... .. ... / .. ... / .- -. / . -..- .- -- .--. .-.. . -.-.-- -') == True)


def test_validate_true_with_spaces():
    assert (MorseDecoder.validate('- .... .. ...   .. ...   .- -.   . -..- .- -- .--. .-.. . -.-.-- -') == True)


def test_validate_true_with_spaces():
    assert (MorseDecoder.validate('I am not a morse code') == False)


def test_safe_decode_true():
    assert (MorseDecoder.safe_decode('- .... .. ... / .. ... / .- -. / . -..- .- -- .--. .-.. . -.-.--') == TEST4)
