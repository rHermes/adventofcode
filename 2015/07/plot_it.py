import fileinput as fi
import graphviz

dot = graphviz.Digraph(comment="wow")
for line in map(str.rstrip, fi.input()):
    if not line:
        continue

    l, r = line.split(" -> ")
    xs = l.split(" ")

    dot.node(r)

    if len(xs) == 1:
        x = xs[0]
        dot.edge(x, r)
        if x.isnumeric():
            dot.node(x, color="blue")

    elif len(xs) == 2:
        op, x = xs
        nm = "pre_{}".format(r)
        dot.node(nm, op, color="yellow")

        dot.edge(nm, r)
        dot.edge(x, nm)

        if x.isnumeric():
            dot.node(x, color="blue")

    elif len(xs) == 3:
        l, op, rm = xs
        if l.isnumeric():
            dot.node("pre_{}_l".format(r), l, color="blue")
            l = "pre_{}_l".format(r)

        if rm.isnumeric():
            dot.node("pre_{}_r".format(r), rm, color="blue")
            rm = "pre_{}_r".format(r)

        nm = "pre_{}".format(r)
        dot.node(nm, op, color="yellow")
        dot.edge(nm, r)

        dot.edge(l, nm)
        dot.edge(rm, nm)


print(dot.source)
