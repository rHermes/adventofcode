def one_round(w, z, a, b, c):

    z_ = int(z/a)

    # w + c is always positive
    # if x == (z % 26) + b
    if ((z % 26) + b) != w:
        return z_ * 26 + w + c
    else:
        return z_

def explore():
    abcs = [
        (1, 13, 8),
        (1, 12, 16),
        (1, 10, 4),
        (26, -11, 1),
        (1, 14, 13),
        (1, 13, 5),
        (1, 12, 0),
        (26, -5, 10),
        (1, 10, 7),
        (26, 0, 2),
        (26, -11, 13),
        (26, -13, 15),
        (26, -13, 14),
        (26, -11, 9)
    ]

    z_pos = {0: tuple()}
    for j, (a, b, c) in enumerate(abcs):
        print("Starting round {} with {}".format(j, len(z_pos)))
        new_pos = {}
        divid = {}
        for z, pth in z_pos.items():
            lk = ((z % 26) + b)
            if 1 <= lk < 10:
                # print("We can skip with {}".format(lk))
                nz = one_round(lk, z, a, b, c)
                npth = pth + (lk,)
                if nz in divid:
                    kl = divid[nz]
                    if kl > npth:
                        divid[nz] = npth
                else:
                    divid[nz] = npth

            for w in range(1,10):
                nz = one_round(w, z, a, b, c)
                npth = pth + (w,)
                if nz in new_pos:
                    kl = new_pos[nz]
                    if kl > npth:
                        new_pos[nz] = npth
                else:
                    new_pos[nz] = npth


        
        if divid:
            z_pos = divid
        else:
            z_pos = new_pos

        
    print(z_pos, print("".join(str(x) for x in z_pos[0])))

explore()


def solve(states):
    x, y, z, w = 0, 0, 0, 0
    abcs = [
        (1, 13, 8),
        (1, 12, 16),
        (1, 10, 4),
        (26, -11, 1),
        (1, 14, 13),
        (1, 13, 5),
        (1, 12, 0),
        (26, -5, 10),
        (1, 10, 7),
        (26, 0, 2),
        (26, -11, 13),
        (26, -13, 15),
        (26, -13, 14),
        (26, -11, 9)
    ]

    for w, (a, b, c) in zip(reversed(states),abcs):
        z = one_round(w, z, a, b, c)
        # print(z)

#     z = one_round(states.pop(), z, 1, 13, 8)
#     z = one_round(states.pop(), z, 1, 12, 16)
#     z = one_round(states.pop(), z, 1, 10, 4)
#     z = one_round(states.pop(), z, 26, -11, 1)
#     z = one_round(states.pop(), z, 1, 14, 13)
#     z = one_round(states.pop(), z, 1, 13, 5)
#     z = one_round(states.pop(), z, 1, 12, 0)
#     z = one_round(states.pop(), z, 26, -5, 10)
#     z = one_round(states.pop(), z, 1, 10, 7)
#     z = one_round(states.pop(), z, 26, 0, 2)
#     z = one_round(states.pop(), z, 26, -11, 13)
#     z = one_round(states.pop(), z, 26, -13, 15)
#     z = one_round(states.pop(), z, 26, -13, 14)
#     z = one_round(states.pop(), z, 26, -11, 9)
    return z





def raw(states):
    x, y, z, w = 0, 0, 0, 0
    w = states.pop()
    x *= 0
    x += z
    x %= 26
    z = int(z/1)
    x += 13
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 8
    y *= x
    z += y
    w = states.pop()
    x *= 0
    x += z
    x %= 26
    z = int(z/1)
    x += 12
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 16
    y *= x
    z += y
    w = states.pop()
    x *= 0
    x += z
    x %= 26
    z = int(z/1)
    x += 10
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 4
    y *= x
    z += y
    w = states.pop()
    x *= 0
    x += z
    x %= 26
    z = int(z/26)
    x += -11
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 1
    y *= x
    z += y
    w = states.pop()
    x *= 0
    x += z
    x %= 26
    z = int(z/1)
    x += 14
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 13
    y *= x
    z += y
    w = states.pop()
    x *= 0
    x += z
    x %= 26
    z = int(z/1)
    x += 13
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 5
    y *= x
    z += y
    w = states.pop()
    x *= 0
    x += z
    x %= 26
    z = int(z/1)
    x += 12
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 0
    y *= x
    z += y
    w = states.pop()
    x *= 0
    x += z
    x %= 26
    z = int(z/26)
    x += -5
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 10
    y *= x
    z += y
    w = states.pop()
    x *= 0
    x += z
    x %= 26
    z = int(z/1)
    x += 10
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 7
    y *= x
    z += y
    w = states.pop()
    x *= 0
    x += z
    x %= 26
    z = int(z/26)
    x += 0
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 2
    y *= x
    z += y
    w = states.pop()
    x *= 0
    x += z
    x %= 26
    z = int(z/26)
    x += -11
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 13
    y *= x
    z += y
    w = states.pop()
    x *= 0
    x += z
    x %= 26
    z = int(z/26)
    x += -13
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 15
    y *= x
    z += y
    w = states.pop()
    x *= 0
    x += z
    x %= 26
    z = int(z/26)
    x += -13
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 14
    y *= x
    z += y
    w = states.pop()
    x *= 0
    x += z
    x %= 26
    z = int(z/26)
    x += -11
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 9
    y *= x
    z += y

    return z

import random

for i in range(1000):
    ll = random.choices(range(1,10), k=14)
    aa = list(ll)
    bb = list(ll)
    nn = raw(aa)
    gg = solve(bb)
    if nn != gg:
        print(ll)
        print(nn, gg)
        

    assert(nn == gg)
