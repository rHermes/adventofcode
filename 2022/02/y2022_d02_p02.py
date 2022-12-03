import fileinput as fi

A_R = "A"
A_P = "B"
A_S = "C"

B_L = "X"
B_D = "Y"
B_W = "Z"

S_ROCK = 1
S_PAPER = 2
S_SCISSOR = 3

S_LOSS = 0
S_DRAW = 3
S_WIN = 6

lookup = {
        f'{A_R} {B_L}': S_LOSS + S_SCISSOR,
        f'{A_R} {B_D}': S_DRAW + S_ROCK,
        f'{A_R} {B_W}': S_WIN + S_PAPER,

        f'{A_P} {B_L}': S_LOSS + S_ROCK,
        f'{A_P} {B_D}': S_DRAW + S_PAPER,
        f'{A_P} {B_W}': S_WIN + S_SCISSOR,

        f'{A_S} {B_L}': S_LOSS + S_PAPER,
        f'{A_S} {B_D}': S_DRAW + S_SCISSOR,
        f'{A_S} {B_W}': S_WIN + S_ROCK,
}

lines = filter(bool, map(str.rstrip, fi.input()))
print(sum(lookup[line] for line in lines))
