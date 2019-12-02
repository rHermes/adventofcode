import fileinput

def solve(lines):
    x, y = 0, 2
    trans = {"U": (0,1), "D": (0, -1), "L": (-1,0), "R": (1,0)}
    # This is in reverse, because my 0,0 is in the bottom left
    keypad = [
            [" ", " ", "D", " ", " "],
            [" ", "A", "B", "C", " "],
            ["5", "6", "7", "8", "9"],
            [" ", "2", "3", "4", " "],
            [" ", " ", "1", " ", " "]
    ]
    code = []
    for line in lines:
        for c in line:
            dx, dy = trans[c]
            nx = min(4,max(0, x+dx))
            ny = min(4,max(0, y+dy))
            if (keypad[ny][nx] != " "):
                x, y = nx, ny

        code.append(keypad[y][x])
    
    return "".join(code)

lines = [x.strip() for x in fileinput.input()]
print(solve(lines))
