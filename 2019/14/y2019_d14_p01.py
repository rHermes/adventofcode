import fileinput
from collections import defaultdict

trans = []
for line in fileinput.input():
    ins, out = line.strip().split("=>")
    
    # Refine ints
    ins = [x.strip().split(" ") for x in ins.strip().split(",")]
    ins = [ (int(a), b) for a, b in ins]

    # Refine outs
    out = out.strip().split(" ")
    out = (int(out[0]), out[1])

    trans.append((ins,out))

need = defaultdict(int)
need["FUEL"] = -2


def get_trans(trans, t):
    for ins, outs in trans:
        if outs[1] == t:
            return (ins, outs)

    return None

def is_atomic(trans, t):
    return get_trans(trans, t) == None


while True:
    for t, am in need.items():
        if am >= 0:
            continue

        tr = get_trans(trans, t)
        if tr is None:
            continue

        ins, out = tr

        while need[t] < 0:
            for (n,i) in ins:
                need[i] -= n

            need[t] += out[0]

        break

    else:
        print("We done")
        break

for k, v in need.items():
    if v == 0:
        continue
    print(" - {}: {}".format(k, v))
