from Decoders.ASCIICipher import ASCIIDecoder
from Decoders.Base64Cipher import Base64Decoder
from Decoders.CaesarCipher import CaesarDecoder
from Decoders.ReverseCipher import ReverseDecoder
from evaluator import evaluate

ciphertext = """Creuncf gur zbfg jryy-choyvpvmrq grpu gbby va Ehffvn'f nefrany sbe svtugvat pbebanivehf vf Zbfpbj'f znffvir snpvny-erpbtavgvba flfgrz. Ebyyrq bhg rneyvre guvf lrne, gur fheirvyynapr flfgrz unq bevtvanyyl cebzcgrq na hahfhny choyvp onpxynfu, jvgu cevinpl nqibpngrf svyvat ynjfhvgf bire haynjshy fheirvyynapr.
Pbebanivehf, ubjrire, unf tvira na harkcrpgrq choyvp-eryngvbaf obbfg gb gur flfgrz.
Ynfg jrrx, Zbfpbj cbyvpr pynvzrq gb unir pnhtug naq svarq 200 crbcyr jub ivbyngrq dhnenagvar naq frys-vfbyngvba hfvat snpvny erpbtavgvba naq n 170,000-pnzren flfgrz. Nppbeqvat gb n Ehffvna zrqvn ercbeg fbzr bs gur nyyrtrq ivbyngbef jub jrer svarq unq orra bhgfvqr sbe yrff guna unys n zvahgr orsber gurl jrer cvpxrq hc ol n pnzren.
"Jr jnag gurer gb or rira zber pnzrenf fb gung gung gurer vf ab qnex pbeare be fvqr fgerrg yrsg," Byrt Onenabi, Zbfpbj'f cbyvpr puvrs, fnvq va n erprag oevrsvat, nqqvat gung gur freivpr vf pheeragyl jbexvat gb vafgnyy na nqqvgvbany 9,000 pnzrenf."""

ciphertext = """Perhaps the most well-publicized tech tool in Russia's arsenal for fighting coronavirus is Moscow's massive facial-recognition system. Rolled out earlier this year, the surveillance system had originally prompted an unusual public backlash, with privacy advocates filing lawsuits over unlawful surveillance.
Coronavirus, however, has given an unexpected public-relations boost to the system.
Last week, Moscow police claimed to have caught and fined 200 people who violated quarantine and self-isolation using facial recognition CTF2020{DSADASDASDAS} and a 170,000-camera system. According to a Russian media report some of the alleged violators who were fined had been outside for less than half a minute before they were picked up by a camera.
"We want there to be even more cameras so that that there is no dark corner or side street left," Oleg Baranov, Moscow's police chief, said in a recent briefing, adding that the service is currently working to install an additional 9,000 cameras."""

base64 = "UGVyaGFwcyB0aGUgbW9zdCB3ZWxsLXB1YmxpY2l6ZWQgdGVjaCB0b29sIGluIFJ1c3NpYSdzIGFyc2VuYWwgZm9yIGZpZ2h0aW5nIGNvcm9uYXZpcnVzIGlzIE1vc2NvdydzIG1hc3NpdmUgZmFjaWFsLXJlY29nbml0aW9uIHN5c3RlbS4gUm9sbGVkIG91dCBlYXJsaWVyIHRoaXMgeWVhciwgdGhlIHN1cnZlaWxsYW5jZSBzeXN0ZW0gaGFkIG9yaWdpbmFsbHkgcHJvbXB0ZWQgYW4gdW51c3VhbCBwdWJsaWMgYmFja2xhc2gsIHdpdGggcHJpdmFjeSBhZHZvY2F0ZXMgZmlsaW5nIGxhd3N1aXRzIG92ZXIgdW5sYXdmdWwgc3VydmVpbGxhbmNlLgpDb3JvbmF2aXJ1cywgaG93ZXZlciwgaGFzIGdpdmVuIGFuIHVuZXhwZWN0ZWQgcHVibGljLXJlbGF0aW9ucyBib29zdCB0byB0aGUgc3lzdGVtLgpMYXN0IHdlZWssIE1vc2NvdyBwb2xpY2UgY2xhaW1lZCB0byBoYXZlIGNhdWdodCBhbmQgZmluZWQgMjAwIHBlb3BsZSB3aG8gdmlvbGF0ZWQgcXVhcmFudGluZSBhbmQgc2VsZi1pc29sYXRpb24gdXNpbmcgZmFjaWFsIHJlY29nbml0aW9uIENURjIwMjB7RFNBREFTREFTREFTfSBhbmQgYSAxNzAsMDAwLWNhbWVyYSBzeXN0ZW0uIEFjY29yZGluZyB0byBhIFJ1c3NpYW4gbWVkaWEgcmVwb3J0IHNvbWUgb2YgdGhlIGFsbGVnZWQgdmlvbGF0b3JzIHdobyB3ZXJlIGZpbmVkIGhhZCBiZWVuIG91dHNpZGUgZm9yIGxlc3MgdGhhbiBoYWxmIGEgbWludXRlIGJlZm9yZSB0aGV5IHdlcmUgcGlja2VkIHVwIGJ5IGEgY2FtZXJhLgoiV2Ugd2FudCB0aGVyZSB0byBiZSBldmVuIG1vcmUgY2FtZXJhcyBzbyB0aGF0IHRoYXQgdGhlcmUgaXMgbm8gZGFyayBjb3JuZXIgb3Igc2lkZSBzdHJlZXQgbGVmdCwiIE9sZWcgQmFyYW5vdiwgTW9zY293J3MgcG9saWNlIGNoaWVmLCBzYWlkIGluIGEgcmVjZW50IGJyaWVmaW5nLCBhZGRpbmcgdGhhdCB0aGUgc2VydmljZSBpcyBjdXJyZW50bHkgd29ya2luZyB0byBpbnN0YWxsIGFuIGFkZGl0aW9uYWwgOSwwMDAgY2FtZXJhcy4="
plaintexts = []
plaintexts += CaesarDecoder(ciphertext)
plaintexts += ASCIIDecoder(ciphertext)
plaintexts += Base64Decoder(ciphertext)
plaintexts += ReverseDecoder(ciphertext)

print(evaluate(plaintexts, 'TFT', 'CTF2020{}')[0])
