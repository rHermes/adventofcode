import fileinput as fi
import re

def parse_rules(rs):
    d = {}
    for line in rs:
        if not line:
            break

        num, rest = line.split(": ")

        if rest[0] == '"':
            d[int(num)] = (True,rest[1:-1])
        else:
            pss = [[int(x) for x in alt.split()] for alt in rest.split(" | ")]
            d[int(num)] = (False, pss)

    return d

# returns a regex that matches num
def build_regex(rules, num, cache):
    if num in cache:
        return cache[num]

    dfs = lambda x: build_regex(rules, x, cache)

    done, alts = rules[num]
    if done:
        ans = alts
    else:
        pos = ["".join(dfs(x) for x in alt) for alt in alts]
        ans = "({})".format("|".join(pos))

    cache[num] = ans
    return ans


G = map(str.rstrip, fi.input())

rules = parse_rules(G)
rule0 = build_regex(rules, 0, {})

# Not really needed, but helps make the program clearer
prog = re.compile("^" + rule0 + "$", flags=re.MULTILINE)

# Find all matches in the rest of the string
print(sum(1 for _ in prog.finditer("\n".join(G))))
