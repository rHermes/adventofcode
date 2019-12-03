import fileinput

# I am sure there is a way that invovles looking at the cube
# of the N to know which lane it is on and using that to find
# where it is, but I just bruteforced it.
def find_pos(n):
    if n == 1:
        return (0,0)

    x, y = 0, 0
    i = 1
    while i < n+1:
        # Initial move to the right
        x += 1
        i += 1
        if i == n:
            return (x,y)
    
        # Going up
        while y < x:
            y += 1
            i += 1
            if i == n:
                return (x,y)
        
        # Going left
        while x > -y:
            x -= 1
            i += 1
            if i == n:
                return (x,y)
        
        # Going down
        while y > x:
            y -= 1
            i += 1
            if i == n:
                return (x,y)
        
        # Going right
        while x < -y:
            x += 1
            i += 1
            if i == n:
                return (x,y)

def solve(n):
    a, b = find_pos(n)
    return abs(a) + abs(b)

for line in fileinput.input():
    print(solve(int(line.rstrip())))
