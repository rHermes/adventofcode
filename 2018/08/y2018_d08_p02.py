import fileinput as fi

def parse(node):
    nchild = node[0]
    nmeta = node[1]

    ch = []
    cc = 2
    for i in range(nchild):
        c, m = parse(node[cc:])
        ch.append(m)
        cc += c

    if nchild == 0:
        mt = sum(node[cc:cc+nmeta])
    else:
        mt = 0
        for m in node[cc:cc+nmeta]:
            if 0 <= m-1 < len(ch):
                mt += ch[m-1]

    return cc + nmeta, mt


_, ans = parse([int(x) for x in next(fi.input()).split()])
print(ans)
