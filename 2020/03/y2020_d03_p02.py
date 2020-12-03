import fileinput


M = []
for line in fileinput.input():
    l = []
    for x in line.rstrip():
        if x == '.':
            l.append(0)
        else:
            l.append(1)
        
    M.append(l)

ans = 1
for (dx, dy) in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
    x, y = 0, 0
    lans = 0
    lans += M[y][x]
    N = len(M[0])
    while y < len(M):
        lans += M[y][x % N]
        y += dy
        x += dx

    if lans > 0:
        ans = ans * lans

        
print(ans)
