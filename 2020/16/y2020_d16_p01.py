import fileinput as fi
import itertools as it

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

fields = parse_fields(lines)

# Now here we could do the smart thing and merge the intervals together to
# check the least amount of them and so forth, but we are going to cheat and
# just create an set.
valid = set()
for (al,ah), (bl, bh) in fields.values():
    valid.update(set(range(al,ah+1)), set(range(bl,bh+1)))

# We skip our ticket this time.
tickets = it.islice(parse_tickets(lines), 1, None)

# Flatten the arrays and sum up to the answer
nums = it.chain.from_iterable(tickets)
print(sum(filter(lambda x: x not in valid, nums)))
