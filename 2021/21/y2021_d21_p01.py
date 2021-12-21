import fileinput as fi

def solve(p1, p2):
    p1 -= 1
    p2 -= 1

    s1, s2 = 0, 0
    dice = 0
    rolls = 0

    turn_p1 = True
    while s1 < 1000 and s2 < 1000:
        forward = dice % 100 + (dice + 1) % 100 + (dice + 2) % 100 + 3
        dice = (dice + 3) % 100
        rolls += 3

        if turn_p1:
            p1 = (p1 + forward) % 10
            s1 += p1 + 1
        else:
            p2 = (p2 + forward) % 10
            s2 += p2 + 1

        turn_p1 = not turn_p1

    if p1 < p2:
        return s1 * rolls
    else:
        return s2 * rolls


p1, p2 = [int(line.split()[-1]) for line in fi.input()]
print(solve(p1, p2))
