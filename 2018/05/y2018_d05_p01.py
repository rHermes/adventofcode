import fileinput as fi

def react(pol):
    buf = []
    for x in pol:
        if buf and buf[-1] == x.swapcase():
            buf.pop()
        else:
            buf.append(x)

    return len(buf)

pol = next(fi.input()).rstrip()
print(react(pol))
