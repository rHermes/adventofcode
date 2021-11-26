import fileinput as fi

def solve(s):
    in_garbage = False
    score = 0
    i = 0

    while i < len(s):
        if s[i] == '!':
            i += 1
        elif in_garbage:
            if s[i] == '>':
                in_garbage = False
            else:
                score += 1
        elif s[i] == '<':
            in_garbage = True

        i += 1

    return score

print(solve(next(fi.input()).rstrip()))
