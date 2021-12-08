import fileinput as fi

# Taken from https://old.reddit.com/r/adventofcode/comments/rbj87a/2021_day_8_solutions/hnouzz3/
# I couldn't do this better myself, but the idea is clever. We use masks of known digits to find
# the next one. This is only possible because we can ensure that all ten digits are going to be on
# the line.
def smart_solve(line):
    words, outs = line.split(" | ")
    clues = [frozenset(x) for x in words.split()]
    _1, _7, _4, *unknown, _8 = sorted(clues, key=len)
    _9 = next(d for d in unknown if len(_4 & d) == 4); unknown.remove(_9)
    _3 = next(d for d in unknown if len(d - _7) == 2); unknown.remove(_3)
    _2 = next(d for d in unknown if len(_9 & d) == 4); unknown.remove(_2)
    _0 = next(d for d in unknown if len(_1 & d) == 2); unknown.remove(_0)
    _6 = next(d for d in unknown if len(d     ) == 6); unknown.remove(_6);
    _5 = next(d for d in unknown)                    ; unknown.remove(_5);

    keys = {"".join(sorted(v)): str(i) for i, v in enumerate([_0, _1, _2, _3, _4, _5, _6, _7, _8, _9])}

    ans = ""
    for word in outs.split():
        ans += keys["".join(sorted(word))]

    return int(ans)

def solve(lines):
    return sum(smart_solve(x) for x in lines)

lines = map(str.rstrip, fi.input())
print(solve(lines))
