import fileinput

def solve(lines):
    x, y = 1, 1
    trans = {"U": (0,1), "D": (0, -1), "L": (-1,0), "R": (1,0)}
    # This is in reverse, because my 0,0 is in the bottom left
    keypad = [
            [7,8,9],
            [4,5,6],
            [1,2,3]
    ]
    code = []
    for line in lines:
        for c in line:
            dx, dy = trans[c]
            x = min(2,max(0, x+dx))
            y = min(2,max(0, y+dy))
        code.append(keypad[y][x])
    
    return "".join([str(c) for c in code])

lines = [x.strip() for x in fileinput.input()]
print(solve(lines))
