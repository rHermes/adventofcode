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



# print(rules_l)
# print(messages)


def parse_rules(rs):
    d = {}
    for num, rest in rs:
        # if num == 8:
        #     rest = "42 | 42 8"
 
        # if num == "11":
        #     rest = "2 31 | 42 11 31"

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
        return things
    
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

    return list(set(poss))
    # return poss

# Returns true if a msg can match a number
# def can_match_rule(rules, num, msg):
#     if num not in rules:


# returns a regex that matches num
def build_regex(rules, num, spec=True):
    if num not in rules:
        raise "WTF!"

    if spec:
        if num == 8:
            return "(" + build_regex(rules, 42, spec) + "+)"
        
        if num == 11:
            p42 = build_regex(rules, 42, spec)
            p31 = build_regex(rules, 31, spec)
            pss = "{}{}".format(p42,p31)
            for x in range(2,16):
                pss += "|{}{{{}}}{}{{{}}}".format(p42,x,p31,x)

            return "(" + pss + ")"


    done, things = rules[num]
    if done:
        return things

    pos = []
    for alt in things:
        ps = ""
        for p in alt:
            ps += build_regex(rules, p, spec)
        
        pos.append(ps)

    return "(" + "|".join(pos) + ")"



rules = parse_rules(rules_l)
# print(rules)

# print(build_regex(rules, 5))
rule0 = build_regex(rules, 0, True)
# print(rule0)
prog = re.compile("^" + rule0 + "$")

ans = 0
for msg in messages:
    if prog.fullmatch(msg):
        ans += 1

print(ans)
