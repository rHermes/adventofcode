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
                    if kl < npth:
                        divid[nz] = npth
                else:
                    divid[nz] = npth

            for w in range(1,10):
                nz = one_round(w, z, a, b, c)
                npth = pth + (w,)
                if nz in new_pos:
                    kl = new_pos[nz]
                    if kl < npth:
                        new_pos[nz] = npth
                else:
                    new_pos[nz] = npth

        if divid:
            z_pos = divid
        else:
            z_pos = new_pos

    print("".join(str(x) for x in z_pos[0]))

explore()
