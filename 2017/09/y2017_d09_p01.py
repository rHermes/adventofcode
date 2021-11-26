import fileinput as fi

def solve(s):
    in_garbage = False
    score = 0
    depth = 0
    i = 0
    while i < len(s):
        if s[i] == '!':
            i += 1
        elif in_garbage:
            in_garbage = s[i] != '>'
        elif s[i] == '<':
            in_garbage = True
        elif s[i] == '{':
            depth += 1
        elif s[i] == '}':
            score += depth
            depth -= 1

        i += 1

    return score

print(solve(next(fi.input()).rstrip()))

