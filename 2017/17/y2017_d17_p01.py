import fileinput as fi
import collections

def solve(step):
    Q = collections.deque([0])

    for i in range(1, 2018):
        Q.rotate(-(step+1))
        Q.appendleft(i)

    return Q[1]

print(solve(int(next(fi.input()).rstrip())))
