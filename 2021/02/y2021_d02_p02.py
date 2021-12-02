import fileinput as fi

hor, dep, aim = 0, 0, 0
for line in fi.input():
    act, b = line.split(" ")
    if act == "forward":
        hor += int(b)
        dep += aim * int(b)
    elif act == "down":
        aim += int(b)
    else:
        aim -= int(b)

print(hor * dep)
