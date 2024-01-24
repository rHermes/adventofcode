import fileinput as fi
import itertools as it
import collections as cs


# Input parsing
INPUT = "".join(fi.input()).rstrip()
lines = list(INPUT.splitlines())
grid = [[c for c in line] for line in lines]
gsz = (len(grid), len(grid[0]))
Y, X = gsz

# ok so we make one HUGE assumption about input, and that is that there is an
# open path to the edges from the Starting point. This is not true for the
# example, but it's true for my input. This allows us to make some simplifications.

# We are partitioning the space into 8 spaces.
#
#    NW | N | NE
#    ---+---+---
#    W  | C | E
#    ---+---+---
#    SW | S | SE
#
# With the assumption above, we know the shortest path to enter any of the squares as
# we go out.

# Return a map
def calcCost(open: set[tuple[int,int]], start: tuple[int,int]):
    cost = {}
    Q = cs.deque([(start, int(0))])
    while Q:
        pos, co = Q.popleft()
        if pos in cost:
            continue

        cost[pos] = co

        py, px = pos
        for np in [(py+1,px), (py-1,px), (py,px+1), (py,px-1)]:
            if np in open and np not in cost:
                Q.append((np, co+1))
    
    return cost

def numSteppedOn(cost: dict[tuple[int,int], int], remainingSteps: int, wantEvens: bool):
    ans = 0
    for (py,px), co in cost.items():
        if co <= remainingSteps and (py + px + wantEvens) % 2 != 0:
            ans += 1

    return ans

open = set()
start = (0, 0)
for y in range(Y):
    for x in range(X):
        c = grid[y][x]
        if c == "S":
            start = (y, x)
            open.add((y,x))
        elif c == ".":
            open.add((y,x))

blockC = (Y//2, X//2)

# The straight directions
blockW = (Y//2, 0)
blockE = (Y//2, X-1)
blockN = (0, X//2)
blockS = (Y-1, X//2)

# Diagonals
blockNW = (0, 0)
blockNE = (0, X-1)
blockSW = (Y-1, 0)
blockSE = (Y-1, X-1)


# Verify assertions about starting conditions
assert(start == blockC)
for y in range(0,Y):
    assert((y, blockC[1]) in open)
for x in range(0,X):
    assert((blockC[0], x) in open)

costC = calcCost(open, blockC)

costW = calcCost(open, blockW)
costE = calcCost(open, blockE)
costN = calcCost(open, blockN)
costS = calcCost(open, blockS)

costNW = calcCost(open, blockNW)
costNE = calcCost(open, blockNE)
costSW = calcCost(open, blockSW)
costSE = calcCost(open, blockSE)


STEPS = 26501365
# STEPS = 1000000000

# We are inserting weirder here, to specify if we want odd or even steps.
WEIRDER = STEPS % 2 == 0

ans = 0

# Any answer must include the center, as we have so many steps, let's begin there
ans += numSteppedOn(costC, STEPS, False != WEIRDER)


# Ok let's just figure out how far we get, in the north direction first.
def calcStraightPlots(firstCost, enterCost, DX):
    maxCost = max(enterCost.values())

    furthestBlockReached = (STEPS - firstCost - 1) // DX
    assert(firstCost + 1 + DX*furthestBlockReached <= STEPS)
    # print(furthestBlockReached)

    maxFullBlock = (STEPS - firstCost - 1 - maxCost) // DX
    assert(firstCost + 1 + DX*maxFullBlock + maxCost <= STEPS)
    # print(maxFullBlock)

    # So we know that all the blocks less or equal to maxFullBlock are full
    steppedOnWhenEven = numSteppedOn(enterCost, STEPS, True != WEIRDER)
    steppedOnWhenOdd = numSteppedOn(enterCost, STEPS, False != WEIRDER)

    if maxFullBlock % 2 == 0:
        numberOfFullOdd = maxFullBlock // 2
        numberOfFullEven = numberOfFullOdd + 1
    else:
        numberOfFullOdd = (maxFullBlock + 1) // 2
        numberOfFullEven = numberOfFullOdd

    # print("In the north there are {} full evens and {} full odds".format(numberOfFullEven, numberOfFullOdd))

    ans = numberOfFullOdd * steppedOnWhenOdd + numberOfFullEven * steppedOnWhenEven

    # Now we just do the half fulls.
    for i in range(maxFullBlock + 1, furthestBlockReached + 1):
        stepsTaken = firstCost + 1 + i*DX
        ans += numSteppedOn(enterCost, STEPS - stepsTaken, (i % 2 == 0) != WEIRDER)

    return ans


def calcSlopePlots(firstCost, enterCost, DX):
    maxCost = max(enterCost.values())

    initialCost = firstCost + 2

    furthestBlockReached = (STEPS - initialCost) //  DX
    assert(initialCost + DX*furthestBlockReached <= STEPS)
    # print(furthestBlockReached)

    maxFullBlock = (STEPS - initialCost - maxCost) // DX
    assert(initialCost + DX*maxFullBlock + maxCost <= STEPS)
    # print(maxFullBlock)


    # So we know that all the blocks less or equal to maxFullBlock are full
    steppedOnWhenEven = numSteppedOn(enterCost, STEPS, True != WEIRDER)
    steppedOnWhenOdd = numSteppedOn(enterCost, STEPS, False != WEIRDER)


    # We can figure out how many odd and even numbers there are here, no
    # need for more iteration.

    timesOdd = 0
    timesEven = 0


    if (maxFullBlock+1) % 2 == 0:
        evenNumbers = (maxFullBlock + 1) // 2
        oddNumbers = evenNumbers
    else:
        evenNumbers = maxFullBlock // 2
        oddNumbers = evenNumbers + 1


    timesEven = evenNumbers*(evenNumbers+1)
    timesOdd = oddNumbers*oddNumbers

    ans = timesOdd * steppedOnWhenOdd + timesEven * steppedOnWhenEven

    # Now we just do the half fulls.
    for i in range(maxFullBlock + 1, furthestBlockReached + 1):
        stepsTaken = initialCost + i*DX
        ans += (i+1)*numSteppedOn(enterCost, STEPS - stepsTaken, (i % 2 != 0) != WEIRDER)

    return ans


plotsN = calcStraightPlots(costC[blockN], costS, Y)
plotsS = calcStraightPlots(costC[blockS], costN, Y)
plotsE = calcStraightPlots(costC[blockE], costW, X)
plotsW = calcStraightPlots(costC[blockW], costE, X)

ans += plotsN
ans += plotsS
ans += plotsE
ans += plotsW

# print("In the north there are {} plots stepped on".format(plotsN))
# print("In the south there are {} plots stepped on".format(plotsS))
# print("In the west there are {} plots stepped on".format(plotsW))
# print("In the east there are {} plots stepped on".format(plotsE))


plotsNW = calcSlopePlots(costC[blockNW], costSE, Y)
plotsNE = calcSlopePlots(costC[blockNE], costSW, Y)
plotsSW = calcSlopePlots(costC[blockSW], costNE, Y)
plotsSE = calcSlopePlots(costC[blockSE], costNW, Y)

# print("In the NW there are {} plots stepped on".format(plotsNW))
# print("In the NE there are {} plots stepped on".format(plotsNE))
# print("In the SW there are {} plots stepped on".format(plotsSW))
# print("In the SE there are {} plots stepped on".format(plotsSE))

ans += plotsNW
ans += plotsNE
ans += plotsSW
ans += plotsSE

print(ans)
