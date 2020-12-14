import fileinput as fi

s = set()
for x in fi.input():
    z = int(x)
    if 2020 - z in s:
        print(z * (2020 - z))
        break

    s.add(z)
