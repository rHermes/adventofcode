import fileinput as fi
import heapq
from graphlib import TopologicalSorter

ts = TopologicalSorter()

for line in fi.input():
    pr = line.split(" ")
    a, b = pr[1], pr[-3]
    ts.add(b, a)

ts.prepare()

EXTRA = 60

# Worker heaps
IDLE = 5
BUSY = []

Q = list(ts.get_ready())
heapq.heapify(Q)

t_min = 0
while ts.is_active():
    # While there are tasks and idle workers, we hand out tasks.
    while Q and IDLE > 0:
        c = heapq.heappop(Q)
        IDLE -= 1

        heapq.heappush(BUSY, (t_min+ord(c)-(ord("A")-1)+EXTRA, c))

    # Now we should pop of the latest task, as there is nothing more to do
    t, c = heapq.heappop(BUSY)
    IDLE += 1

    # New lowest watermark
    t_min = t

    ts.done(c)
    for x in ts.get_ready():
        heapq.heappush(Q, x)

print(t_min)
