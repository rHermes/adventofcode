import fileinput as fi

def parse(node):
    nchild = node[0]
    nmeta = node[1]

    mt = 0
    cc = 2
    for i in range(nchild):
        m, c = parse(node[cc:])
        mt += m
        cc += c

    mt += sum(node[cc:cc+nmeta])
    cc += nmeta

    return (mt, cc)


ans, _= parse([int(x) for x in next(fi.input()).split()])
print(ans)
