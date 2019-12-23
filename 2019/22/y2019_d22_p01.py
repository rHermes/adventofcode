import fileinput

# Returns the deck
def solve(insts, N=10007):
    deck = list(range(N))

    for inst in insts:
        if inst == "deal into new stack":
            deck = list(reversed(deck))
            # print(deck)
        elif inst.startswith("cut"):
            n = int(inst[3:])
            if n < 0:
                n = N + n

            deck = deck[n:] + deck[:n]
        elif inst.startswith("deal with increment"):
            kk = len("deal with increment ")
            ix = int(inst[kk:])

            # deck = [deck[(i*ix) % N] for i in range(N)]
            newdeck = list(range(N))
            for i, c in enumerate(deck):
                newdeck[(i*ix) % N] = c

            deck = newdeck

        else:
            raise Exception("Don't know inst: {}".format(inst))

    return deck


insts = [line.strip() for line in fileinput.input()]
deck = solve(insts)
print(deck.index(2019))
# print(deck)
