import fileinput as fi
import itertools as it
from math import prod

# I know I could have used regex here, but I prefer to not use it for very
# simple inputs like this, where it just adds overhead.
def parse_range(x):
    l, h = x.split("-")
    return (int(l), int(h))

def parse_field(line):
    *names, a, _, b = line.split(" ")
    return (" ".join(names)[:-1], parse_range(a), parse_range(b))

def parse_fields(lines):
    fields = {}
    for line in lines:
        if not line:
            return fields

        name, a, b = parse_field(line)
        fields[name] = (a,b)

    raise "Invalid input!"

# Returns an iterator for your and the nearby tickets
def parse_tickets(lines):
    for line in lines:
        # Just skip other lines
        if not line or line[0] in "yn":
            continue

        yield [int(x) for x in line.split(",")]

lines = map(str.rstrip, fi.input())

# We should build and interval tree here, but we just can't be bothered
fields = parse_fields(lines)
tickets = parse_tickets(lines)

our_ticket = None
fields_pos = {name: set(range(len(fields))) for name in fields.keys()}
for ticket in tickets:
    if our_ticket is None:
        our_ticket = ticket

    changes = []
    for (i,x) in enumerate(ticket):
        valid = 0
        for name, ((al,ah), (bl,bh)) in fields.items():
            if al <= x <= ah or bl <= x <= bh:
                valid += 1
            else:
                changes.append((name,i))

        if valid == 0:
            break
    else:
        # We made it all the way through, now we need to apply the changes
        for name, i in changes:
            fields_pos[name].remove(i)

taken = set()
positions = {}
while len(positions) != len(fields):
    for field, fpos in fields_pos.items():
        ppos = fpos - taken
        if len(ppos) == 1:
            x = ppos.pop()
            positions[field] = x
            taken.add(x)


print(prod(our_ticket[v] for k,v in positions.items() if k.startswith("departure")))
