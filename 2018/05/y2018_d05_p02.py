import fileinput as fi
import re

def matcher():
    alph = 'abcdefghijklmnopqrstuvwxyz'
    exp = []
    for x in alph:
        exp.append(x + x.upper())
        exp.append(x.upper() + x)

    prog = "|".join(exp)
    return prog


def pred(pol):
    mtch = matcher()
    while True:
        pol, new = re.subn(mtch, "", pol)
        if new == 0:
            return pol
    
pol = next(fi.input()).rstrip()
mm = None
for a in 'abcdefghijklmnopqrstuvwxyz':
    tpol = pol.replace(a,"").replace(a.upper(), "")
    rpol = pred(tpol)
    if mm == None or len(rpol) < mm:
        print("New shortest is {} with {}".format(a, len(rpol)))
        mm = len(rpol)


print(mm)
