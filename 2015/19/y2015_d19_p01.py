import fileinput as fi

import collections

INPUT = "".join(fi.input()).rstrip()

groups = INPUT.split("\n\n")

reps = collections.defaultdict(set)
for line in groups[0].splitlines():
    i, o = line.split(" => ")
    reps[i].add(o)

atom = groups[1]

pos = set()
for i in range(len(atom)):
    before = atom[:i]
    cur = atom[i:]

    for k, repss in reps.items():
        if cur.startswith(k):
            after = atom[i+len(k):]
            for rep in repss:
                pos.add(before + rep + after)


print(len(pos))
