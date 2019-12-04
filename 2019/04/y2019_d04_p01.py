import fileinput



s = "272091-815432"

n = 0
for x in range(272091, 815432):
    y = [int(c) for c in str(x)]
    if y != sorted(y):
        continue
    
    found = False
    for i in range(len(y)-1):
        if y[i] == y[i+1]:
            found = True
            break
    
    if not found:
        continue

    n += 1

print(n)
