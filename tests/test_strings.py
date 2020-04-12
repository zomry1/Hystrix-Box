from Tools.strings import strings

TEST1 = r'''JFIF
ICC_PROFILE
lcms
mntrRGB XYZ 
.acspAPPL
-lcms
desc
8cprt
Nwtpt
chad
,rXYZ
bXYZ
gXYZ
rTRC
 gTRC
 bTRC
 chrm
$mluc
enUS
mluc
enUS
XYZ 
-sf32
XYZ 
XYZ 
XYZ 
para
[para
[para
[chrm
2BQRaq
45FSTcestu
&'7CDEU
2ABQaq
1bfw
DDDDDDDDDEI
VBBcq
DTHz
7>DEV}}/
}DDDDDDDDDDV.
?'j(9d
rTtN#
|-F &
uZ"*t
YqU""""""""""""""""""""""""""*D
DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDE
Zh-1q2z
ffn_
qxG.
M4^t
GX2q
5,qj
db09@
NJ3QLv
 *}=kbk
]gAgl
y,m~
k~.Au
{J5q
,g`h
ne]\
YQQYPu5u
MJ_`
TPOb
*Goy
r88e
?U$C
 u_S
\m,4
b'm^L
K75Uv
z6;U
:e <
b}_{
=,Yfd-
JIx;t4
gwx\;.
^IGp
$qF[
bM&0
s]3szr
|7^-
4b`M
,;OSz
[I5-La4
erKe3
VTNu
-z$s
<6JQ
wpY[>
=U$d
jcjr
02gl
dqc 
jGak\7^y
)n;<
qDd[U
""".+
hh&6o)K
#YEE1
3}*Ks
lI,$@ak
3._<
Z{'!
1\W|
Tq,7
_E6A#K
>e{r
3|TRTD
L$<]
wI#*at
~-+!
i~$^
/w)rz
UA3}j
}Y-'u
E"aj5
;>Nk
nN}J
UA41j|
|*xS
K3w:0~+n
Uoclz
}F]\
jgz)
wV>J
=gJ"
nvD=
6K}u
k3ut
bJc>
ggo$
$i6}saa
,038
"9|A
'l'\
bx*A
3pvb
E$T2
BLru
:Rcl
s%cdw
x[>7
>=S6
i;t<i
R3e7r
]ESOIu
Bx~i
jN=yr
}Y(#
k#'oc>j
;GX=]T
rdTD
'$~K
m.ss
g}\Y
WW\&y
Pl;|
DDXaY
+L| 
>4~XB
/5mQ
T8`0
\i3]
Wc{"
Gx}2
}Gfv
!u:%
rz\)
x4t`u
$_5yj7
rN"ucF
Rnpj
=$q}yjU=6
*AMK
.7\M_S&|
SF90
e85q
GR9,`Tp
o##C
yBmB
<MUP>+S
IGu~
SDDDT
_}H[
}E%2o#""/
B9jvl&U
"""""""""""""""""""""""""*H
%R"'&EoW
i~yf
"""""""""/>d
DDDDDDDDEl)
|c6O
_d>5
>bx+
\DEl
DDDDDDDDDD^9
DDDDDDDDDDV
DDDE'''

TEST2 = '''ICC_PROFILE
mntrRGB XYZ 
DDDDDDDDDEI
}DDDDDDDDDDV.
YqU""""""""""""""""""""""""""*D
DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDE
"""""""""""""""""""""""""*H
"""""""""/>d
DDDDDDDDEl)
DDDDDDDDDD^9
DDDDDDDDDDV'''

TEST3 = '''YqU""""""""""""""""""""""""""*D
DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDE
"""""""""""""""""""""""""*H'''


def test_strings_4chars():
    assert (strings('../examples/strings.jpg') == TEST1)


def test_strings_11chars():
    assert (strings('../examples/strings.jpg', 11) == TEST2)


def test_strings_20chars():
    assert (strings('../examples/strings.jpg', 20) == TEST3)


def test_strings_100chars():
    assert (strings('../examples/strings.jpg', 100) == '')


def test_strings_noFile():
    assert (strings('') == '')


def test_strings_emptyFile():
    assert (strings('../examples/empty') == '')
