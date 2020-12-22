import fileinput as fi
from itertools import takewhile, islice
from collections import deque

def get_cards():
    G = map(str.strip, fi.input())
    p1d = deque(map(int, takewhile(bool, islice(G,1,None))))
    p2d = deque(map(int, takewhile(bool, islice(G,1,None))))
    return p1d, p2d

# This returns the object we use to lookup in the hash
def zsig(p1d, p2d):
    return (tuple(p1d), tuple(p2d))

# Returns True for p1d and False for p2d
# modifies both p1d and p2d. Seen is a set
def game(p1d, p2d, seen):
    while p1d and p2d:
        zs = zsig(p1d, p2d)
        if zs in seen:
            return True
        seen.add(zs)

        p1, p2 = p1d.popleft(), p2d.popleft()

        if p1 <= len(p1d) and p2 <= len(p2d):
            z1d = deque(islice(p1d, p1))
            z2d = deque(islice(p2d, p2))
            winner = game(z1d, z2d, set())
        else:
            winner = p2 < p1

        if winner:
            p1d.extend((p1, p2))
        else:
            p2d.extend((p2, p1))

    return bool(p1d)


p1d, p2d = get_cards()
game(p1d, p2d, set())

ans = 0
for i, x in enumerate(reversed(p1d or p2d), 1):
    ans += i*x
print(ans)
