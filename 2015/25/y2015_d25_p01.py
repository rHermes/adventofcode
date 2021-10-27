import fileinput as fi

# idx calculates the index of number in a given column and row. We know that
# the first row of the sheet of paper, are all triangle numbers. Thus we have
#
# idx(c, 1) = (c * (c+1) / 2)
#
# For a given row r, we can then follow the pattern until we reach the next
# number in row 1. Since we go one up and one to the right on each step, it
# will take r-1 steps to get to 1.
#
# We know that this number is (r-1) bigger than the answer we want, so the
# formula is then:
#
# idx(c, r) = idx(c + (r-1), 1) - (r-1)
# idx(c, r) = ((c + r - 1) * (c + r)) // 2 - r + 1
#
# Which is our final answer.
def idx(c, r):
    return ((c+r-1) * (c+r))//2 - r + 1

# We can use Modular exponentiation to calculate the answer here. We know
# that for each step until the row, we will be multiplicating with B and
# doing it modulo M. Since we do this idx(c, r) - 1 times, the first step
# is simply S, we can factor the multiplications out, which we arrive at
# the expression S * B**(idx(c, r) - 1) mod M
def solve(col, row, S=20151125):
    M = 33554393
    B = 252533

    return (S * pow(B, idx(col, row) - 1, M)) % M


words = next(fi.input()).split()
row = int(words[words.index("row")+1][:-1])
column = int(words[words.index("column")+1][:-1])

print(solve(column, row))
