import fileinput as fi
import heapq
from graphlib import TopologicalSorter

ts = TopologicalSorter()

for line in fi.input():
    pr = line.split(" ")
    a, b = pr[1], pr[-3]
    ts.add(b, a)

ts.prepare()

ans = ""

Q = list(ts.get_ready())
heapq.heapify(Q)

while Q:
    c = heapq.heappop(Q)
    ans += c

    ts.done(c)
    for x in ts.get_ready():
        heapq.heappush(Q, x)

print(ans)
