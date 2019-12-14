import fileinput
import math


def sign(n):
    if n < 0:
        return -1
    if n > 0:
        return 1
    else:
        return 0

def one_dim_step(s,dim):
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            k = dim
            w = sign(s[i][k] - s[j][k])
            s[i][k+3] += -1*w
            s[j][k+3] += w

    for i in range(len(s)):
        k = dim
        s[i][k] += s[i][k+3]

    return s


def lcm(a,b):
    return abs(a*b)//math.gcd(a,b)

# Read in state
state = []
for line in fileinput.input():
    s = line.strip()[1:-1].split(", ")
    planet  = [0,0,0,0,0,0]
    for kv in s:
        c, v = kv.split("=")
        v = int(v)
        idx = {"x": 0, "y": 1, "z": 2}[c]
        planet[idx] = v

    state.append(planet)

# We need to find the period for each axis, since they are independent
ans = 1
first_state = [x[:] for x in state]
for k in range(3):
    orig_pos = tuple(x[k] for x in first_state)
    orig_vel = tuple(x[k+3] for x in first_state)
    for i in range(1,10000000000000):
        state = one_dim_step(state,k)
        new_pos = tuple(x[k] for x in state)
        if new_pos == orig_pos:
            new_vel =  tuple(x[k+3] for x in state)
            if orig_vel == new_vel:
                break
    
    ans = lcm(ans, i)

print(ans)
