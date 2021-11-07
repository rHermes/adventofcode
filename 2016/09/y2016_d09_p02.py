import fileinput as fi


def solve(line):
    s = 0
    while True:
        idx = line.find("(")
        if idx < 0:
            return s + len(line)

        x, line = line[idx+1:].split(")", maxsplit=1)
        size, times = map(int, x.split("x"))

        s += idx + times*solve(line[:size])

        line = line[size:]


for line in map(str.rstrip, fi.input()):
    if line:
        print(solve(line))
