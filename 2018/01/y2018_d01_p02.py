import fileinput as fi
import itertools as it

seen = {0}
xs = it.accumulate(it.cycle(map(int,fi.input())))
for f in xs:
    if f in seen:
        break
    seen.add(f)

print(f)
