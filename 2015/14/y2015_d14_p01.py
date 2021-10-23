import fileinput as fi

def calc(speed, act, rest, N=2503):
    dist = 0
    sec = 0
    while sec < N:
        dist += min(act*speed, (N-sec)*speed)
        sec += act + rest

    return dist

dists = []
for line in map(str.rstrip, fi.input()):
    if not line:
        continue
    prts = line.split()
    speed, act, rest = int(prts[3]), int(prts[6]), int(prts[13])
    dists.append(calc(speed, act, rest))

print(max(dists))
