import fileinput as fi

mem = {}
for line in fi.input():
    l, r = line.rstrip().split(" = ")
    if l == "mask":
        mask_and = (1<<36)-1
        mask_or = 0
        for i, c in enumerate(reversed(r)):
            if c == '1':
                mask_or |= 1 << i
            elif c == '0':
                mask_and ^= (1 << i)

    else:
        dst, val = int(l[4:-1]), int(r)
        mem[dst] = (val & mask_and) | mask_or

print(sum(mem.values()))
