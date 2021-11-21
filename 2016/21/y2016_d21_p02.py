import fileinput as fi
import itertools as it
import collections


def solve(inp, lines):
    for line in lines:
        parts = line.split(" ")
        if line.startswith("swap position"):
            src = int(parts[2])
            dst = int(parts[-1])
            x = list(inp)
            x[src], x[dst] = x[dst], x[src]
            inp = "".join(x)
        elif line.startswith("swap letter"):
            a = parts[2]
            b = parts[-1]
            inp = inp.replace(a,"ø").replace(b,a).replace("ø",b)
        elif line.startswith("reverse"):
            a = int(parts[2])
            b = int(parts[-1])
            x = list(inp)
            while a < b:
                x[a], x[b] = x[b], x[a]
                a += 1
                b -= 1
            inp = "".join(x)
        elif line.startswith("rotate based on"):
            let = parts[-1]
            adx = inp.index(let)
            if adx >= 4:
                adx += 1

            x = collections.deque(inp)
            x.rotate(1 + adx)
            inp = "".join(x)
        elif line.startswith("move"):
            src = int(parts[2])
            dst = int(parts[-1])
            get = inp[src]
            x = list(inp)
            del x[src]
            x.insert(dst, get)
            inp = "".join(x)
        elif line.startswith("rotate"):
            ll = [-1, 1][parts[1] == "right"]
            idx = int(parts[-2])
            x = collections.deque(inp)
            x.rotate(idx*ll)
            inp = "".join(x)

    return inp

# Input parsing
INPUT = "".join(fi.input()).rstrip()
lines = list(INPUT.splitlines())

for a in map("".join, it.permutations("abcdefgh")):
    if solve(a, lines) == "fbgdceah":
        print(a)
        break
