import fileinput as fi
import re


def parse_rules(rs):
    d = {}
    for line in rs:
        if not line:
            break

        num, rest = line.split(": ")
        if rest[0] == '"':
            d[num] = rest[1:-1]
        else:
            d[num] = [alt.split() for alt in rest.split(" | ")]

    return d

# returns a regex that matches num
def build_regex(rules, num, cache):
    if num in cache:
        return cache[num]

    dfs = lambda x: build_regex(rules, x, cache)

    alts = rules[num]
    if type(alts) == str:
        ans = alts
    else:
        pos = ["".join(dfs(x) for x in alt) for alt in alts]
        if len(pos) == 1:
            ans = pos[0]
        else:
            ans = "(?:{})".format("|".join(pos))

    cache[num] = ans
    return ans

G = map(str.rstrip, fi.input())

rules = parse_rules(G)
rule0 = "^{}$".format(build_regex(rules, "0", {}))

# Find all matches in the rest of the string
print(sum(1 for _ in re.finditer(rule0, "\n".join(G), flags=re.MULTILINE)))
