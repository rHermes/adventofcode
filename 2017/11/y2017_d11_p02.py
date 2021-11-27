import fileinput as fi

di = {
    "n": -1j,
    "ne": 1 - 1j,
    "se": 1,
    "s": 1j,
    "sw": -1 + 1j,
    "nw": -1,
}

def axial_from_zero(a):
    return int((abs(a.real) + abs(a.real + a.imag) + abs(a.imag)) // 2)

def solve(s):
    steps = s.split(",")
    pt = 0
    ans = 0
    for stp in steps:
        pt += di[stp]
        ans = max(ans, axial_from_zero(pt))

    return ans


print(solve(next(fi.input()).rstrip()))
