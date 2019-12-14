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


def total_energy(state):
    ans = 0
    for p in state:
        xs = [abs(x) for x in p]
        ans += sum(xs[:3]) * sum(xs[3:])

    return ans


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

for i in range(1000):
    state = step(state)

print(total_energy(state))
