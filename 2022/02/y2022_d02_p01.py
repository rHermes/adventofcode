import fileinput as fi

A_R = "A"
A_P = "B"
A_S = "C"

B_R = "X"
B_P = "Y"
B_S = "Z"

S_ROCK = 1
S_PAPER = 2
S_SCISSOR = 3

S_LOSS = 0
S_DRAW = 3
S_WIN = 6

lookup = {
        f'{A_R} {B_R}': S_DRAW + S_ROCK,
        f'{A_R} {B_P}': S_WIN + S_PAPER,
        f'{A_R} {B_S}': S_LOSS + S_SCISSOR,
        f'{A_P} {B_R}': S_LOSS + S_ROCK,
        f'{A_P} {B_P}': S_DRAW + S_PAPER,
        f'{A_P} {B_S}': S_WIN + S_SCISSOR,
        f'{A_S} {B_R}': S_WIN + S_ROCK,
        f'{A_S} {B_P}': S_LOSS + S_PAPER,
        f'{A_S} {B_S}': S_DRAW + S_SCISSOR,
}

lines = filter(bool, map(str.rstrip, fi.input()))
print(sum(lookup[line] for line in lines))
