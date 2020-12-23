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
print(len(pred(pol)))
