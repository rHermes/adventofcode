import fileinput
from collections import defaultdict
from tqdm import tqdm


def get_trans(trans, t):
    for ins, outs in trans:
        if outs[1] == t:
            return (ins, outs)

    return None

def is_atomic(trans, t):
    return get_trans(trans, t) == None



def solve_for_fuel(trans, n, need=None):
    if need is None:
        need = defaultdict(int)
        need["FUEL"] = -1*n

    while True:
        for t, am in need.items():
            if am >= 0:
                continue

            if t not in trans:
                continue

            out_am, ins = trans[t]

            while need[t] < 0:
                for (n,i) in ins:
                    need[i] -= n

                need[t] += out_am

            break

        else:
            return need


trans = {}
for line in fileinput.input():
    ins, out = line.strip().split("=>")
    
    # Refine ints
    ins = [x.strip().split(" ") for x in ins.strip().split(",")]
    ins = [ (int(a), b) for a, b in ins]

    # Refine outs
    out = out.strip().split(" ")
    out = (int(out[0]), out[1])

    trans[out[1]] = (int(out[0]), ins)

ORE = 1000000000000
MAX = 100000000000000000000000000000
LEAP = 10000

need = None
prev = 0
pro = tqdm(total=ORE)
for i in range(MAX):
    need = solve_for_fuel(trans, 1, need)
    ndd = -1*need["ORE"]
    if i % 1000 == 0:
        pass
        # print("We need {} for {} which is {} away".format(ndd, i, ORE-ndd))
    if ndd > ORE:
        break


    #heu = [(k,v) for (k,v) in need.items() if v != 0]
    #if len(heu) < 8:
    #    print(i)
    #if need["XNWV"] == 0:
    #    print(i)
    
    need["FUEL"] = -1
    pro.update(ndd-prev)
    prev = ndd

print(i)

# for i in range(1,MAX,LEAP):
#     nds = solve_for_fuel(trans, i)
#     ndd = -1*nds["ORE"]
#     print("We need {} for {} which is {} away".format(ndd, i, ORE-ndd))
#     if ndd > ORE:
#         break

# print("it in the neightboorhood of {}".format(i))


# for j in range(i-LEAP, i):
#     nds = solve_for_fuel(trans, j)
#     print("We need {} for {}".format(-1*nds["ORE"], j))
#     if -1*nds["ORE"] > ORE:
#         break


#need["FUEL"] = -1
# print(j)
