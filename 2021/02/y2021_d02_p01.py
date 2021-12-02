import fileinput as fi

hor, dep = 0, 0
for line in fi.input():
    act, b = line.split(" ")
    if act == "forward":
        hor += int(b)
    elif act == "down":
        dep += int(b)
    else:
        dep -= int(b)

print(hor * dep)
