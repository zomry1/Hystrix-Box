from CaesarCipher import CaesarDecreptor
from SanityCheck import evaluation
from WordCheck import evaluateSentence
from FormatCheck import checkFormat,returnFlags

ciphertext = """Creuncf gur zbfg jryy-choyvpvmrq grpu gbby va Ehffvn'f nefrany sbe svtugvat pbebanivehf vf Zbfpbj'f znffvir snpvny-erpbtavgvba flfgrz. Ebyyrq bhg rneyvre guvf lrne, gur fheirvyynapr flfgrz unq bevtvanyyl cebzcgrq na hahfhny choyvp onpxynfu, jvgu cevinpl nqibpngrf svyvat ynjfhvgf bire haynjshy fheirvyynapr.
Pbebanivehf, ubjrire, unf tvira na harkcrpgrq choyvp-eryngvbaf obbfg gb gur flfgrz.
Ynfg jrrx, Zbfpbj cbyvpr pynvzrq gb unir pnhtug naq svarq 200 crbcyr jub ivbyngrq dhnenagvar naq frys-vfbyngvba hfvat snpvny erpbtavgvba naq n 170,000-pnzren flfgrz. Nppbeqvat gb n Ehffvna zrqvn ercbeg fbzr bs gur nyyrtrq ivbyngbef jub jrer svarq unq orra bhgfvqr sbe yrff guna unys n zvahgr orsber gurl jrer cvpxrq hc ol n pnzren.
"Jr jnag gurer gb or rira zber pnzrenf fb gung gung gurer vf ab qnex pbeare be fvqr fgerrg yrsg," Byrt Onenabi, Zbfpbj'f cbyvpr puvrs, fnvq va n erprag oevrsvat, nqqvat gung gur freivpr vf pheeragyl jbexvat gb vafgnyy na nqqvgvbany 9,000 pnzrenf."""

'''
ciphertext = """Creuncf gur zbfg jryy-choyvpvmrq grpu gbby va Ehffvn'f nefrany sbe svtugvat pbebanivehf vf Zbfpbj'f znffvir snpvny-erpbtavgvba flfgrz. Ebyyrq bhg rneyvre guvf lrne, gur fheirvyynapr flfgrz unq bevtvanyyl cebzcgrq na hahfhny choyvp onpxynfu, jvgu cevinpl nqibpngrf svyvat ynjfhvgf bire haynjshy fheirvyynapr.
Pbebanivehf, ubjrire, unf tvira na harkcrpgrq choyvp-eryngvbaf obbfg gb gur flfgrz.
Ynfg jrrx, Zbfpbj cbyvpr pynvzrq gb unir pnhtug naq svarq 200 crbcyr jub ivbyngrq dhnenagvar naq frys-vfbyngvba hfvat snpvny erpbtavgvba naq n 170,000-pnzren flfgrz. Nppbeqvat gb n Ehffvna zrqvn ercbeg fbzr bs gur nyyrtrq ivbyngbef jub jrer svarq unq orra bhgfvqr sbe yrff guna unys n zvahgr orsber gurl jre"""
ciphertext = """rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr"""
'''
#ciphertext = 'FNQFN QNF NF NFQ NFQ NQ JDNQ JNQ JN SPGS2020{QFNQFNQQFQNFQNF} NFQNFQF NQNF NFQ NF QDQ FNQ DJ QFNIQF ERSTJR NQJD '
plaintexts = CaesarDecreptor(ciphertext)

evaluations = []
#Evaluate each plaintext and calculate error
for plaintext in plaintexts:
	evaluations.append((plaintext[:20], returnFlags('CTF2020{}',plaintext)))

#Sort plaintext by error level
evaluations = sorted(evaluations, key=lambda x: x[1])
#Print summery of each plaintext and error
print('\n'.join([str(element) for element in evaluations]))