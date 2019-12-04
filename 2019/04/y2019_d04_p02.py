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
            behind_thing = False
            before_thing = False
            if i+2 < len(y):
                if y[i+2] == y[i]:
                    behind_thing = True

            if i-1 > -1:
                if y[i-1] == y[i]:
                    before_thing = True

            if not (behind_thing or before_thing):
                found = True
    
    if not found:
        continue
    
    n += 1

print(n)
