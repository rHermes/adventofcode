import fileinput as fi

# Parse input
mem = {}
mask_or = 0
mask_float = []
for line in fi.input():
    l, r = line.rstrip().split(" = ")
    if l == "mask":
        mask_or = 0
        mask_float.clear()
        floating = []
        for i, c in enumerate(reversed(r)):
            if c == '1':
                mask_or |= 1 << i
            elif c == 'X':
                floating.append(i)

        for i in range(2**(len(floating))):
            mand = (1 << 36) - 1
            mor = 0
            for (j, elem) in enumerate(floating):
                if i & (1 << j):
                    mor |= 1 << elem
                else:
                    mand ^= 1 << elem

            mask_float.append((mand, mor))

    else:
        dst, val = int(l[4:-1]), int(r)
        mdst = dst | mask_or
        for mand, mor in mask_float:
            mdst = (mdst & mand) | mor
            mem[mdst] = val

print(sum(mem.values()))
