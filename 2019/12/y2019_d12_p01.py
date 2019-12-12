import fileinput


def sign(n):
    if n < 0:
        return -1
    if n > 0:
        return 1
    else:
        return 0


def step(s):
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            for k in range(3):
                w = sign(s[i][k] - s[j][k])
                s[i][k+3] += -1*w
                s[j][k+3] += w

    for i in range(len(s)):
        for k in range(3):
            s[i][k] += s[i][k+3]

    return s




def energy(s):
    ans = 0
    for p in s:
        pp = [abs(x) for x in p]
        wow  = sum(pp[:3]) * sum(pp[3:])
        ans += wow

    return ans



state = [[7,10,17,0,0,0], [-2,7,0,0,0,0], [12,5,12,0,0,0],[5,-8,6,0,0,0]]
#state = [[-1,0,2,0,0,0], [2,-10,-7,0,0,0], [4,-8,8,0,0,0],[3,5,-1,0,0,0]]


for i in range(1000):
    state = step(state)


print(energy(state))
