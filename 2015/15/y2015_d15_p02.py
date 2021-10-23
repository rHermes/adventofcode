import fileinput as fi
import math


def get_combs(left, n):
    if n == 1:
        yield [left]
    else:
        for x in range(left+1):
            for y in get_combs(left-x, n-1):
                yield [x] + y


def calc_score(times, ings):
    s = [0 for _ in ings[0]]
    for time, ing in zip(times, ings):
        for i in range(len(s)):
            s[i] += time*ing[i]

    return math.prod(map(lambda x: max(x, 0), s))


INPUT = "".join(fi.input()).rstrip()
lines = list(INPUT.splitlines())

xs = []
cals = []
for line in lines:
    xx = [int(x.split()[-1]) for x in line.split(", ")]
    xs.append(xx[:-1])
    cals.append(xx[-1])

ans = 0
for x in get_combs(100, len(xs)):
    scal = sum(num * cal for (num, cal) in zip(x, cals))
    if scal != 500:
        continue

    sco = calc_score(x, xs)
    if ans < sco:
        ans = sco

print(ans)
