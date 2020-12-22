import fileinput as fi
from itertools import takewhile, islice
from collections import deque

def get_cards():
    G = map(str.strip, fi.input())
    p1d = deque(map(int, takewhile(bool, islice(G,1,None))))
    p2d = deque(map(int, takewhile(bool, islice(G,1,None))))
    return p1d, p2d

p1d, p2d = get_cards()

while p1d and p2d:
    p1, p2 = p1d.popleft(), p2d.popleft()
    if p2 < p1:
        p1d.extend((p1, p2))
    else:
        p2d.extend((p2, p1))

ans = 0
for i, x in enumerate(reversed(p1d or p2d), 1):
    ans += i*x
print(ans)
