import fileinput as fi

lines = [x.rstrip() for x in fi.input()]

def select(lines, crit):
    left = [x for x in lines]
    j = 0
    while len(left) > 1:
        ones = [x for x in left if x[j] == "1"]
        zeros = [x for x in left if x[j] == "0"]
        if crit(len(zeros), len(ones)):
            left = zeros
        else:
            left = ones

        j += 1

    return int(left[0], 2)

ox = select(lines, lambda z, o: z > o)
co = select(lines, lambda z, o: z <= o)
print(ox * co)
