import fileinput as fi

def checksum(s):
    chk = ""
    for i in range(0, len(s), 2):
        x, y = s[i], s[i+1]
        if x == y:
            chk += "1"
        else:
            chk += "0"

    if len(chk) % 2 == 0:
        return checksum(chk)
    else:
        return chk

def solve(s, n):
    while len(s) < n:
        s += "0" + "".join(['1', '0'][x == '1'] for x in reversed(s))

    return checksum(s[:n])

print(solve(next(fi.input()).rstrip(), 272))
