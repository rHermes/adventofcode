import fileinput as fi

LIMIT = int(next(fi.input()))
UL = LIMIT//11 + 1

data = [0 for _ in range(UL)]

for x in range(1, UL+1):
    for y, _ in zip(range(x, UL+1, x), range(50)):
        data[y-1] += x

    if data[x-1]*11 >= LIMIT:
        break

print(x)
