import fileinput as fi
import collections as cs

N = cs.defaultdict(int)

for line in map(str.rstrip, fi.input()):
    pre, post = line.split(" | ")
    ticket = frozenset(int(x) for x in post.split(" ") if x)

    pre, post = pre.split(": ")
    winners = frozenset(int(x) for x in post.split(" ") if x)
    game = int(pre.split(" ")[-1])
    
    # We have one more of this card now
    N[game] += 1
    
    overlap = len(winners & ticket)
    for ogame in range(game+1, game+overlap+1):
        # For each of the new cards, we get one new of them, for
        # each instance of the current card we have.
        N[ogame] += N[game]

print(sum(N.values()))
