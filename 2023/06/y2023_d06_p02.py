import fileinput as fi
import re
import math

def ways_to_win(time, dist):
    # So if we say that this is function f(x)
    
    # f(x) = x * (t - x)
    #
    # where t is the total time of the race
    #
    # d < f(x)
    # d < x * (t - x)

    # d < x*t - x**2
    # 0 < -x**2 + t*x - d
    #
    # this is a system of unknowns of ax**2 + bx +c
    #
    # a = -1, b = t, c = -d
    #
    # which we can solve with the quadratic equation.


    # under square
    temp = time**2 - 4 * dist
    if temp < 0:
        return 0

    temp = math.sqrt(temp)

    over1 = math.ceil((time - temp) / 2)
    over2 = math.floor((time + temp) / 2)

    # we need to check if they are exact, and if so, remove them.
    if dist == over1*(time - over1):
        over1 += 1
    
    if dist == over2*(time - over2):
        over2 -= 1
        
    return over2 - over1 + 1

# Input parsing
numbers = [re.findall("[0-9]+", line) for line in fi.input()]

time = ""
dist = ""
for t, d in zip(numbers[0], numbers[1]):
    time += t
    dist += d

print(ways_to_win(int(time), int(dist)))
