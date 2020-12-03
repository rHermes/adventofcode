import fileinput

ans = 0

M = []
for line in fileinput.input():
    l = []
    for x in line.rstrip():
        if x == '.':
            l.append(0)
        else:
            l.append(1)
        
    M.append(l)


x, y = 0, 0
ans += M[y][x]
N = len(M[0])
while y < len(M):
    ans += M[y][x % N]
    y += 1
    x += 3
    
print(ans)
