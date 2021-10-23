import fileinput as fi


INPUT = "".join(fi.input()).rstrip()
lines = list(INPUT.splitlines())

known = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

for line in lines:
    pname, facts = line[4:].split(":", maxsplit=1)

    idents = [x.split(": ") for x in facts.strip().split(", ")]
    for k, val in idents:
        if known[k] != int(val):
            break
    else:
        print(pname)
