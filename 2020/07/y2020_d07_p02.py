import fileinput
from functools import lru_cache

BAGS = {}
for line in fileinput.input():
    bag, rst = line.rstrip()[:-1].split(" bags contain ")
    cons = {}
    if rst != "no other bags":
        for obags in rst.split(", "):
            n, *xs, _ = obags.split(" ")
            cons[" ".join(xs)] = int(n)

    BAGS[bag] = cons

# We use dynamic programming here, to avoid recomputing values
# we have previously computed
@lru_cache(None)
def sum_up(bag):
    return sum(n * (sum_up(b)+1) for (b,n) in BAGS[bag].items())

print(sum_up("shiny gold"))
