import fileinput as fi
import collections
import hashlib

def solve(s):
    Q = collections.deque()

    Q.append(((0,0), ""))

    seen = set()
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    dirsl = "UDLR"
    long_ans = ""
    while len(Q) > 0:
        (px, py), pth = Q.popleft()

        if (px, py) == (3, 3):
            if len(pth) > len(long_ans):
                long_ans = pth

            continue

        if pth in seen:
            continue
        seen.add(pth)


        hsh = hashlib.md5((s + pth).encode("latin1")).hexdigest()[:4]

        for i, x in enumerate(hsh):
            dx, dy = dirs[i]
            if x in "bcdef" and 0 <= px + dx < 4 and 0 <= py + dy < 4:
                Q.append(((px + dx, py + dy), pth + dirsl[i]))

    return len(long_ans)


print(solve(next(fi.input()).rstrip()))
