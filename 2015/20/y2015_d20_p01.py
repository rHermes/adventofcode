import fileinput as fi

LIMIT = int(next(fi.input()))
UL = LIMIT//10

data = [0 for _ in range(UL)]

for x in range(1, UL+1):
    for y in range(x, UL+1, x):
        data[y-1] += x

    if data[x-1]*10 >= LIMIT:
        break

print(x)
