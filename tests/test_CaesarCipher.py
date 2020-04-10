from Decoders.CaesarCipher import CaesarDecoder


def test_validate():
    assert (CaesarDecoder.validate() == True)


SAFE_DECODE_RESULT = ['Ij uijt jt b uftu!', 'Jk vjku ku c vguv!', 'Kl wklv lv d whvw!', 'Lm xlmw mw e xiwx!',
                      'Mn ymnx nx f yjxy!', 'No znoy oy g zkyz!', 'Op aopz pz h alza!', 'Pq bpqa qa i bmab!',
                      'Qr cqrb rb j cnbc!', 'Rs drsc sc k docd!', 'St estd td l epde!', 'Tu ftue ue m fqef!',
                      'Uv guvf vf n grfg!', 'Vw hvwg wg o hsgh!', 'Wx iwxh xh p ithi!', 'Xy jxyi yi q juij!',
                      'Yz kyzj zj r kvjk!', 'Za lzak ak s lwkl!', 'Ab mabl bl t mxlm!', 'Bc nbcm cm u nymn!',
                      'Cd ocdn dn v ozno!', 'De pdeo eo w paop!', 'Ef qefp fp x qbpq!', 'Fg rfgq gq y rcqr!',
                      'Gh sghr hr z sdrs!']


def test_safe_decode_true():
    assert (CaesarDecoder.safe_decode('Hi this is a test!') == SAFE_DECODE_RESULT)
