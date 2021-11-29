import fileinput as fi
import heapq

def solve(comps):
    Q = [(0, frozenset(), 0)]
    al = frozenset(range(len(comps)))

    best_ans = 0
    while 0 < len(Q):
        score, used, need = heapq.heappop(Q)
        if score < best_ans:
            best_ans = score

        for i in al - used:
            ca, cb = comps[i]
            if ca == need:
                nneed = cb
            elif cb == need:
                nneed = ca
            else:
                continue

            heapq.heappush(Q, (score - (ca + cb), used.union((i,)), nneed))


    return -best_ans

comps = []
for line in map(str.rstrip, fi.input()):
    a, b = map(int,line.split("/"))
    comps.append((a,b))

print(solve(comps))
