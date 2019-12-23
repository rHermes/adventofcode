import fileinput

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


# Returns the deck
def solve(deck, insts):
    deck = len(deck)

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

# reverse pos i
def reverse_pos(insts, I, N=119315717514047):
    # reverse the ints
    P = I
    for inst in reversed(insts):
        if inst == "deal into new stack":
            P = N - P - 1
        elif inst.startswith("cut"):
            n = int(inst[3:])

            # reverse the path
            n = -n
            if n < 0:
                n = N + n

            P = (P + n) % N

        elif inst.startswith("deal with increment"):
            kk = len("deal with increment ")
            ix = int(inst[kk:])
            
            kk = modinv(ix, N)
            P = (kk*P) % N

        else:
            raise Exception("Don't know inst: {}".format(inst))
    
    return P




insts = [line.strip() for line in fileinput.input()]

#deck = list(range(119315717514047))
#for x in range(101741582076661):
#   deck = solve(insts)
# print(deck.index(2020))
# print(deck)


# cur = 2020
# for i in range(101741582076661):
#     if (i % 10000) == 0:
#         print(i, cur)
#     cur = reverse_pos(insts, cur)


things = {}
cur = 2020
while cur not in things:
    things[cur] = reverse_pos(insts, cur)
    cur = things[cur]




