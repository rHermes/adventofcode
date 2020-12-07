import fileinput
from functools import lru_cache

BAGS = {}
for line in fileinput.input():
    bag, rst = line.rstrip()[:-1].split(" bags contain ")
    cons = set()
    if rst != "no other bags":
        for obags in rst.split(", "):
            cons.add(" ".join(obags.split(" ")[1:-1]))

    BAGS[bag] = cons

# We use dynamic programming here, to avoid recomputing values
# we have previously computed
@lru_cache(None)
def can_contain(bag):
    return bag == "shiny gold" or any(map(can_contain, BAGS[bag]))

print(sum(map(can_contain, BAGS)) - 1)
