import fileinput as fi

def react(pol):
    buf = []
    for x in pol:
        if buf and buf[-1] == x.swapcase():
            buf.pop()
        else:
            buf.append(x)

    return "".join(buf)

pol = next(fi.input()).rstrip()

# We can do the reduction before continuing, because removing characters
# will never remove reduction possibilitis, only add new ones.
pol = react(pol)
mm = None
for c in set(pol.lower()):
    tpol = pol.replace(c,"").replace(c.upper(), "")
    rpol = react(tpol)
    if mm == None or len(rpol) < mm:
        mm = len(rpol)


print(mm)
