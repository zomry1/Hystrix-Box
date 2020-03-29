from CeasarCipher import CaesarDecreptor
from SantiyCheck import Decoder
ciphertext = 'Up fodpef tusjoht dpoubjojoh tqbdft boe vqqfs dbtf mfuufst, vtf uif cvjmu-jo dpefdt mjcsbsz.'
ciphertext1 = """Creuncf gur zbfg jryy-choyvpvmrq grpu gbby va Ehffvn'f nefrany sbe svtugvat pbebanivehf vf Zbfpbj'f znffvir snpvny-erpbtavgvba flfgrz. Ebyyrq bhg rneyvre guvf lrne, gur fheirvyynapr flfgrz unq bevtvanyyl cebzcgrq na hahfhny choyvp onpxynfu, jvgu cevinpl nqibpngrf svyvat ynjfhvgf bire haynjshy fheirvyynapr.
Pbebanivehf, ubjrire, unf tvira na harkcrpgrq choyvp-eryngvbaf obbfg gb gur flfgrz.
Ynfg jrrx, Zbfpbj cbyvpr pynvzrq gb unir pnhtug naq svarq 200 crbcyr jub ivbyngrq dhnenagvar naq frys-vfbyngvba hfvat snpvny erpbtavgvba naq n 170,000-pnzren flfgrz. Nppbeqvat gb n Ehffvna zrqvn ercbeg fbzr bs gur nyyrtrq ivbyngbef jub jrer svarq unq orra bhgfvqr sbe yrff guna unys n zvahgr orsber gurl jrer cvpxrq hc ol n pnzren.
"Jr jnag gurer gb or rira zber pnzrenf fb gung gung gurer vf ab qnex pbeare be fvqr fgerrg yrsg," Byrt Onenabi, Zbfpbj'f cbyvpr puvrs, fnvq va n erprag oevrsvat, nqqvat gung gur freivpr vf pheeragyl jbexvat gb vafgnyy na nqqvgvbany 9,000 pnzrenf."""
plaintexts = CaesarDecreptor(ciphertext1)

answers = []
for plaintext in plaintexts:
	answers.append((plaintext[:20], Decoder(plaintext)))

answers = sorted(answers, key=lambda x: x[1])
print('\n'.join([str(element) for element in answers]))