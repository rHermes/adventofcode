import fileinput as fi
import collections as cs
from multiprocessing import Pool

def countPossible(springs, nums):
    """
    The idea here is taken straight from:
    https://github.com/ConcurrentCrab/AoC/blob/main/solutions/12-2.go

    which again is from:
    https://old.reddit.com/r/adventofcode/comments/18ge41g/2023_day_12_solutions/kd3rclt/

    The idea here is that we loop over a NDFA, but we keep all possible states in memory
    at once. This makes the solution O(n) and the state maps are very small for the given
    inputs.

    The poster was inspired by the techniques described in the following blog posts:
    https://swtch.com/%7Ersc/regexp/regexp1.html
    https://research.swtch.com/glob

    It is a very clever solution and I'm much happier with this one, than the
    memoization solution I had before.
    """
    curStates = cs.defaultdict(int)
    nextStates = cs.defaultdict(int)

    # string index, nums index, continuous run, want a dot next
    curStates[(0,0,0,False)] = 1

    ans = 0
    while curStates:
        for state, num in curStates.items():
            si, ni, cc, expdot = state
            if si == len(springs):
                if ni == len(nums):
                    ans += num

                continue

            c = springs[si]
            if c in "#?" and ni < len(nums) and not expdot:
                # We are still looking for broken springs
                if c == "?" and cc == 0:
                    nextStates[(si + 1, ni, 0, False)] += num

                cc += 1
                if cc == nums[ni]:
                    ni += 1
                    cc = 0
                    expdot = True

                nextStates[(si + 1, ni, cc, expdot)] += num


            elif c in ".?" and cc == 0:
                # We are not in a contiguous row of broken springs
                nextStates[(si + 1, ni, 0, False)] += num

        # This is just to keep the memory low, we could also just
        # deallocate the nextStates completely.
        curStates, nextStates = nextStates, curStates
        nextStates.clear()

    return ans

def solve(line, N=5):
    springs, nu = line.split()
    new_springs = "?".join([springs] * N)
    new_nu = ",".join([nu] * N)
    nums = tuple(int(x) for x in new_nu.split(","))

    return countPossible(new_springs, nums)


lines = [line.rstrip() for line in fi.input()]

# We do this in parallel, because we can
pool = Pool()
results = pool.map(solve, lines)
print(sum(results))
