from HystrixBox.Utils.searchFlag import searchFlag


def test_search_flag_with_spaces():
    assert (searchFlag('zomry1CTF{}','Hi there is zomry1CTF{This_is_an_example} an flag here?') == ['zomry1CTF{This_is_an_example}'])


def test_search_flag_without_spaces():
    assert (searchFlag('zomry1CTF{}','Hi there iszomry1CTF{This_is_an_example}an flag here?') == ['zomry1CTF{This_is_an_example}'])
