import fileinput as fi

INPUT = "".join(fi.input()).rstrip()
lines = list(INPUT.splitlines())

known = {
    "children": lambda x: x == 3,
    "cats": lambda x: x > 7,
    "samoyeds": lambda x: x == 2,
    "pomeranians": lambda x: x < 3,
    "akitas": lambda x: x == 0,
    "vizslas": lambda x: x == 0,
    "goldfish": lambda x: x < 5,
    "trees": lambda x: x > 3,
    "cars": lambda x: x == 2,
    "perfumes": lambda x: x == 1,
}

for line in lines:
    pname, facts = line[4:].split(":", maxsplit=1)

    idents = [x.split(": ") for x in facts.strip().split(", ")]
    for k, val in idents:
        if not known[k](int(val)):
            break
    else:
        print(pname)
