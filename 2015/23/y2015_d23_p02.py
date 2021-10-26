import fileinput as fi

lines = list("".join(fi.input()).rstrip().splitlines())

reg = {"a": 1, "b": 0}

i = 0
while 0 <= i < len(lines):
    ins, *de = lines[i].split()

    if ins == "hlf":
        reg[de[0]] //= 2
        i += 1
    elif ins == "tpl":
        reg[de[0]] *= 3
        i += 1
    elif ins == "inc":
        reg[de[0]] += 1
        i += 1
    elif ins == "jmp":
        i += int(de[0])
    elif ins == "jie":
        if reg[de[0][0]] % 2 == 0:
            i += int(de[1])
        else:
            i += 1
    elif ins == "jio":
        if reg[de[0][0]] == 1:
            i += int(de[1])
        else:
            i += 1

print(reg["b"])
