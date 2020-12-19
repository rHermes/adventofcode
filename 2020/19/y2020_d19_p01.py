import fileinput as fi

import re
import itertools as it
import functools as ft

import more_itertools as mit

import z3
import collections

import math

# findall
# search
# parse
from parse import *

lines = []

rules_l = []
G = map(str.rstrip, fi.input())
for line in G:
    if not line:
        break

    
    num, rest = parse("{:d}: {}", line).fixed
    rules_l.append((num,rest))

messages = []
for line in G:
    if line:
        messages.append(line)


# Convert to map



print(rules_l)
print(messages)


def parse_rules(rs):
    d = {}
    for num, rest in rs:
        if rest[0] == '"':
            d[num] = (True,rest[1:-1])
        else:
            pss = []
            alts = rest.split(" | ")
            for alt in alts:
                ps = [int(x) for x in alt.split(" ")]
                pss.append(ps)
            d[num] = (False, pss)

    return d

# Gives a set of possibilities
def expand_rule(rules, num):
    if num not in rules:
        raise "WTF!"

    done, things = rules[num]
    if done:
        return [things]
    
    # List of strings
    poss = []
    for alt in things:
        # list of strings
        pss = expand_rule(rules, alt[0])

        for p in alt[1:]:
            # A list of strings
            pkk = expand_rule(rules, p)

            pss = [a + b for a,b in it.product(pss, pkk)]


        poss.extend(pss)

    return poss

rules = parse_rules(rules_l)
print(rules)

poss = set(expand_rule(rules, 0))

ans = 0
for msg in messages:
    if msg in poss:
        ans += 1

print(ans)


