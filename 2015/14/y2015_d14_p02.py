import fileinput as fi

def calc(speed, act, rest, n=2503):
    dist = [0]
    sec = 0
    while sec < n:
        i = 0
        while i < act and sec < n:
            dist.append(dist[-1] + speed)
            i += 1
            sec += 1

        j = 0
        while j < rest and sec < n:
            dist.append(dist[-1])
            j += 1
            sec += 1

    return dist[1:]


def points(dists):
    pnts = [0 for _ in dists]
    for x in zip(*dists):
        mm = max(x)
        for i, y in enumerate(x):
            if y == mm:
                pnts[i] += 1

    return pnts

dists = []
for line in map(str.rstrip, fi.input()):
    if not line:
        continue
    prts = line.split()
    speed, act, rest = int(prts[3]), int(prts[6]), int(prts[13])
    dists.append(calc(speed, act, rest))

print(max(points(dists)))
