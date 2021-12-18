import fileinput as fi
import itertools as it
import math
from ast import literal_eval
from copy import deepcopy

# list, val, dir
def add_on(w, x, left):
    a, b = w
    al = isinstance(a, list)
    bl = isinstance(b, list)

    if left:
        if al:
            add_on(a, x, left)
        else:
            w[0] += x
    else:
        # Right
        if bl:
            add_on(b, x, left)
        else:
            w[1] += x

    

def explodes(w, depth=0):
    a, b = w
    al = isinstance(a, list)
    bl = isinstance(b, list)

    if depth == 3 and (al or bl):
        if al:
            l, r = a[0], a[1]
            w[0] = 0

            if not bl:
                w[1] += r
            else:
                add_on(w[1], r, left=True)
            r = None

            return (l,r)
        else:
            assert(bl)

            l, r = b[0], b[1]
            w[1] = 0

            if not al:
                w[0] += l
            else:
                add_on(w[0], l, left=False)
            l = None

            return (l, r)
        
        raise Exception("Not supposed to happen")

    
    if al:
        kk = explodes(a, depth+1)
        if kk is not None:
            l, r = kk
            if l is not None:
                assert(r is None)
                return (l,r)

            if r is not None:
                assert(l is None)

                if bl:
                    add_on(b, r, left=True)
                else:
                    w[1] += r

                return (None, None)

            return (None, None)

    if bl:
        kk = explodes(b, depth+1)
        if kk is not None:
            l, r = kk
            if r is not None:
                assert(l is None)
                return (l,r)

            if l is not None:
                assert(r is None)

                if al:
                    add_on(a, l, left=False)
                else:
                    w[0] += l

                return (None, None)

            return (None, None)

    return None

def splits(w):
    a, b = w
    al = isinstance(a, list)
    bl = isinstance(b, list)

    if al:
        k = splits(a)
        if k:
            return True
    else:
        if 9 < a:
            l =a//2
            r = int(math.ceil(a/2))
            w[0] = [l, r]
            return True

    if bl:
        k = splits(b)
        if k:
            return True
    else:
        if 9 < b:
            l =b//2
            r = int(math.ceil(b/2))
            w[1] = [l, r]
            return True
    
    return False


def reduce(w):
    # We repetedly do both
    while True:
        if explodes(w, depth=0) is not None:
            continue

        if splits(w):
            continue

        break

def sadd(a, b):
    w = [a,b]
    reduce(w)
    return w

def mag(w):
    ans = 0
    a, b = w
    al = isinstance(a, list)
    bl = isinstance(b, list)
    if al:
        ans += 3*mag(a)
    else:
        ans += 3*a

    if bl:
        ans += 2*mag(b)
    else:
        ans += 2*b

    return ans

def solve(nums):
    lmag = 0
    for (a,b) in it.permutations(nums,r=2):
        aw = deepcopy(a)
        bw = deepcopy(b)
        kk = sadd(aw, bw)
        kw = mag(kk)
        if lmag < kw:
            lmag = kw

    return lmag

nums = [literal_eval(x.rstrip()) for x in fi.input()]
print(solve(nums))
