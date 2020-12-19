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

    if num == 8:
        ans = "(?:{}+)".format(dfs(42))

    elif num == 11:
        p42 = dfs(42)
        p31 = dfs(31)
        pss = "{}{}".format(p42,p31)
        for x in range(2,10):
            pss += "|{}{{{}}}{}{{{}}}".format(p42,x,p31,x)

        ans = "(?:" + pss + ")"

    else:
        done, alts = rules[num]
        if done:
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
rule0 = "^{}$".format(build_regex(rules, 0, {}))

# Find all matches in the rest of the string
print(sum(1 for _ in re.finditer(rule0, "\n".join(G), flags=re.MULTILINE)))
