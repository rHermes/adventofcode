import fileinput

REQUIRED = frozenset(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))
OPTIONAL = frozenset(("cid",))
HCL = frozenset("0123456789abcdef")
ECL = frozenset(("amb", "blu", "brn", "gry", "grn", "hzl", "oth"))

# We solve this with an iterator to keep the memory requirements
def passports():
    c = {} 
    for l in fileinput.input():
        l = l.rstrip()
        if l == "":
            yield c
            c.clear()
        else:
            for pair in l.split():
                key, val = pair.split(":", maxsplit=1)
                c[key] = val

    yield c

# Validators
def valid_num(r, lo, hi):
    return r.isnumeric() and lo <= int(r) <= hi

def valid_height(h):
    num, unit = h[:-2], h[-2:]
    if unit == "cm":
        return valid_num(num, 150, 193)
    elif unit == "in":
        return valid_num(num, 59, 76)
    else:
        return False

def valid_hcl(h):
    return len(h) == 7 and h[0] == '#' and set(h[1:]) <= HCL

def valid_pid(p):
    return len(p) == 9 and p.isnumeric()

def valid(p):
    # We want to make sure that no invalid keys are in there
    v = (frozenset(p.keys()) - OPTIONAL) == REQUIRED

    v = v and valid_num(p["byr"], 1920, 2002)
    v = v and valid_num(p["iyr"], 2010, 2020)
    v = v and valid_num(p["eyr"], 2020, 2030)
    v = v and valid_height(p["hgt"])
    v = v and valid_hcl(p["hcl"])
    v = v and p["ecl"] in ECL
    v = v and valid_pid(p["pid"])

    return v


print(sum(map(valid, passports())))
