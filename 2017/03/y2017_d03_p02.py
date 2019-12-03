import fileinput

# Return the value of a field
def val_pos(mem, x, y):
    return (mem.get((x-1,y+1), 0) 
        + mem.get((x, y+1), 0)
        + mem.get((x+1, y+1), 0)
        + mem.get((x-1, y), 0)
        + mem.get((x+1, y), 0)
        + mem.get((x-1, y-1), 0)
        + mem.get((x, y-1), 0)
        + mem.get((x+1, y-1), 0))

def solve(n):
    if n == 1:
        return 1

    x, y = 0, 0
    mem = {(0,0): 1}

    while True:
        x += 1
        mem[(x,y)] = val_pos(mem, x, y)
        if mem[(x,y)] > n:
            return mem[(x,y)]
    
        # Going up
        while y < x:
            y += 1
            mem[(x,y)] = val_pos(mem, x, y)
            if mem[(x,y)] > n:
                return mem[(x,y)]
        
        # Going left
        while x > -y:
            x -= 1
            mem[(x,y)] = val_pos(mem, x, y)
            if mem[(x,y)] > n:
                return mem[(x,y)]
        
        # Going down
        while y > x:
            y -= 1
            mem[(x,y)] = val_pos(mem, x, y)
            if mem[(x,y)] > n:
                return mem[(x,y)]
        
        # Going right
        while x < -y:
            x += 1
            mem[(x,y)] = val_pos(mem, x, y)
            if mem[(x,y)] > n:
                return mem[(x,y)]

for line in fileinput.input():
    print(solve(int(line.rstrip())))
