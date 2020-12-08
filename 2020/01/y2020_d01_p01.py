import fileinput as fi

s = set()
for z in (int(x) for x in fi.input()):
    if 2020 - z in s:
        print(z * (2020 - z))
        break

    s.add(z)
