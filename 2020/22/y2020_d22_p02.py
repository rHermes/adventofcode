import fileinput as fi
from itertools import takewhile, islice

def get_cards():
    G = map(str.strip, fi.input())
    p1d = list(map(int, takewhile(bool, islice(G,1,None))))
    p2d = list(map(int, takewhile(bool, islice(G,1,None))))
    return p1d, p2d

# Returns True for p1d and False for p2d
# modifies both p1d and p2d. Seen is a set
def game(p1d, p2d, seen):
    while p1d and p2d:
        zs = tuple(p1d)
        if zs in seen:
            return True
        seen.add(zs)

        p1, p2 = p1d.pop(0), p2d.pop(0)

        if p1 <= len(p1d) and p2 <= len(p2d):
            winner = game(p1d[:p1], p2d[:p2], set())
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
