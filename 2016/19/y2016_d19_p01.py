import fileinput as fi
import collections

# My cleaned up solution
def solve(n):
    elves = collections.deque(range(1,n+1))

    while len(elves) > 1:
        elves.rotate(-1)
        elves.popleft()

    return elves[0]

# https://en.wikipedia.org/wiki/Josephus_problem#Bitwise
def fast_solve(n):
    b = bin(n)
    # We use b[2] instead of 1 here, to get a 0 if the whole string is zero
    winner = b[3:] + b[2]
    return int(winner,2)


print(fast_solve(int(next(fi.input()))))
