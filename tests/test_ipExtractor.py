from Extractors.ipExtractor import IPExtractor

TEXT = '''@@ -0,0 +1,5 @@
Creuncf gur zbfg jryy-choyvpvmrq grpu gbby va Ehffvn'f nefrany sbe svtugvat pbebanivehf vf Zbfpbj'f znffvir snpvny-erpbtavgvba flfgrz. Ebyyrq bhg rneyvre guvf lrne, gur fheirvyynapr flfgrz unq bevtvanyyl cebzcgrq na hahfhny choyvp onpxynfu, jvgu cevinpl nqibpngrf svyvat ynjfhvgf bire haynjshy fheirvyynapr.
Pbebanivehf, ubjrire, unf tvira na harkcrpgrq choyvp-eryngvbaf obbfg gb gur flfgrz. null@gmail.com
http://www.google.com
Ynfg jrrx, Zbfpbj cbyvpr pynvzrq gb zomry1@gmail.com pnhtug naq svarq 200 cr 2001:db8:0:8d3:0:8a2e:70:7344 gvar naq frys-vfbyngvba hfvat snpvny erpbtavgvba PGS2020{QFNQNFQNFQNF} naq n 170,000-pnzren flfgrz. Nppbeqvat gb n Ehffvna zrqvn ercbeg fbzr bs gur nyyrtrq ivbyngbef jub jrer svarq unq orra bhgfvqr sbe yrff guna unys n zvahgr orsber gurl jrer cvpxrq hc ol n pnzren.
"Jr jnag gurer gb or rira zber pnzrenf fbvf ab qnex pbeare be fvqr fgerrg yrsg," 124.27.1.1 Byrt Onenabi, Zbfpbj'f cbyvpr puvrs, fnvq va n erprag oevrsvat, nqqvat gung gur freivpr vf pheeragyl jbexvat gb vafgnyy na nqqvgvbany 9,000 pnzrenf.
'''

def test_extract():
    assert (IPExtractor.extract(TEXT) == ['124.27.1.1', '2001:db8:0:8d3:0:8a2e:70:7344'])
