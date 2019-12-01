import fileinput

def solve(s):
    seen = set()
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
    seen.add((0,0))
    for inst in insts:
        seen.add((x,y))

        turn = inst[0]
        times = int(inst[1:])

        seen.add((x,y))
        face = trans[face][turn]
        dx, dy = move[face]

        for _ in range(times):
            x += dx
            y += dy
            if (x,y) in seen:
                return abs(x) + abs(y)
            
            seen.add((x,y))


test_cases = [("R8, R4, R4, R8", 4)]

for t, e in test_cases:
    assert(solve(t) == e)

ans = 0
for line in fileinput.input():
    ans += solve(line)

print(ans)
