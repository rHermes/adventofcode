import fileinput

def solve(s):
    trans = {
            "N": {"L": "W", "R": "E" },
            "E": {"L": "N", "R": "S" },
            "S": {"L": "E", "R": "W" },
            "W": {"L": "S", "R": "N" }
            }
    move = {
            "N": (0,1),
            "E": (1,0),
            "S": (0,-1),
            "W": (-1,0)
            }
    face = "N"
    x, y = 0, 0
    insts = s.split(", ")
    for inst in insts:
        turn = inst[0]
        times = int(inst[1:])

        face = trans[face][turn]
        dx, dy = move[face]
        x += dx*times
        y += dy*times

    return abs(x) + abs(y)

test_cases = [("R2, L3", 5), ("R2, R2, R2", 2), ("R5, L5, R5, R3", 12)]

for t, e in test_cases:
    assert(solve(t) == e)

ans = 0
for line in fileinput.input():
    ans += solve(line)

print(ans)
