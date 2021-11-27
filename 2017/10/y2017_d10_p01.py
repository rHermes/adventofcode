import fileinput as fi
import collections

def knot_hash(ins):
    ar = list(range(256))
    c = 0
    skip = 0
    cur = 0
    for l in ins:
        ar[:l] = ar[:l][::-1]
        bw = collections.deque(ar)
        bw.rotate(-(l + skip))
        cur += l + skip
        ar = list(bw)
        skip += 1

    # We must rewind it
    bw = collections.deque(ar)
    bw.rotate(cur)
    return list(bw)

al = knot_hash([int(x) for x in next(fi.input()).rstrip().split(",")])
print(al[0] * al[1])
