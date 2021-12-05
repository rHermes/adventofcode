import fileinput as fi
import collections

def solve(players, last):
    q = collections.deque([0])
    ps = [0 for _ in range(players)]

    for i in range(1, last+1):
        if i % 23 == 0:
            play = (i-1) % players
            ps[play] += i
            q.rotate(7)
            ps[play] += q.popleft()
        else:
            q.rotate(-2)
            q.appendleft(i)

    return max(ps)

inp = next(fi.input()).split()
players, last = int(inp[0]), int(inp[-2])

print(solve(players, last))
