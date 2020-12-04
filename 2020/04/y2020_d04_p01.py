import fileinput


REQUIRED = frozenset(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))
OPTIONAL = frozenset(("cid",))

# We want to make sure that no invalid keys are in there
def valid(s):
    return (s - OPTIONAL) == REQUIRED

# We solve this with an iterator to keep the memory requirements
def passports():
    c = set()
    for l in fileinput.input():
        l = l.rstrip()
        if l == "":
            yield c
            c.clear()
        else:
            for pair in l.split():
                c.add(pair.split(":")[0])

    yield c

print(sum(map(valid, passports())))
