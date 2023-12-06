import fileinput as fi

ans = 0
for line in map(str.rstrip, fi.input()):
    pre, post = line.split(" | ")
    ticket = frozenset(int(x) for x in post.split(" ") if x)

    pre, post = pre.split(": ")
    winners = frozenset(int(x) for x in post.split(" ") if x)
    game = int(pre.split(" ")[-1])

    overlap = len(winners & ticket)
    if overlap:
        ans += 2**(overlap-1)

print(ans)
