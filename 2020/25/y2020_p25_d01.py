import fileinput as fi

card, door = [int(x) for x in fi.input()]

M = 20201227
v = 1
for i in range(1,M+1):
    v = (v*7) % M
    if v == card:
        print(pow(door,i,M))
    elif v == door:
        print(pow(card,i,M))
    else:
        continue
    break
