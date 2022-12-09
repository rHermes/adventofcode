import fileinput as fi

NUM_KNOTS = 10

sign = lambda x: -1 if x < 0 else (1 if x > 0 else 0)

def step(head, tail):
    if abs(head - tail) < 2:
        return tail

    tail += sign(head.real - tail.real)
    tail += sign(head.imag - tail.imag) * 1j
    return tail

DIRS = {"D": -1j, "R": 1, "L": -1, "U": 1j}
knots = [0 for _ in range(NUM_KNOTS)]
visited = {0}

lines = filter(bool, map(str.rstrip, fi.input()))

for line in lines:
    dir, amount = line.split(" ")
    odelta  = DIRS[dir]
    amount = int(amount)
    for _ in range(amount):
        knots[0] += odelta
        for i in range(1,NUM_KNOTS):
            knots[i] = step(knots[i-1], knots[i])

        visited.add(knots[-1])

print(len(visited))
