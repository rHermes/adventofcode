import fileinput
import itertools as it
from collections import defaultdict, deque


def get_params(ops, eip, base, nargs, last_dst=False):
    op = ops[eip]
    ddd = ("{:0" + str(nargs+2) + "}").format(op)
    parms = list(reversed([int(x) for x in ddd[:-2]]))

    if last_dst and parms[-1] == 1:
        raise Exception("With last destination, you cannot have an intermedite value")

    outs = []
    for i, x in enumerate(parms):
        a = ops[eip+1+i]
        if x == 0:
            if last_dst and i == (len(parms)-1):
                outs.append(a)
            else:
                outs.append(ops[a])
        elif x == 1:
            outs.append(a)
        elif x == 2:
            if last_dst and i == (len(parms)-1):
                outs.append(a+base)
            else:
                outs.append(ops[a+base])
        else:
            raise Exception("Not a valid instruction")

    return outs


class IntCode:

    def __init__(self, ops):
        self.ops = defaultdict(int)
        for i, x in enumerate(ops):
            self.ops[i] = x


        self.inputs = []
        self.outputs = []
        self.eip = 0
        self.base = 0
    
    def run(self):
        # returns an event
        while True:
            op = self.ops[self.eip]
            bop = op % 100

            if bop == 1: # ADD 
                a, b, dst = get_params(self.ops, self.eip, self.base, 3, last_dst=True)
                self.ops[dst] = a + b
                self.eip += 4

            elif bop == 2: # MULT
                a, b, dst = get_params(self.ops, self.eip, self.base, 3, last_dst=True)
                self.ops[dst] = a * b
                self.eip += 4

            elif bop == 3: # INPUT
                dst, = get_params(self.ops, self.eip, self.base, 1, last_dst=True)

                if len(self.inputs) == 0:
                    return "input"
                
                ins = self.inputs.pop(0)
                self.ops[dst] = ins
                self.eip += 2
            
            elif bop == 4: # OUTPUT
                src, = get_params(self.ops, self.eip, self.base, 1)
                self.outputs.append(src)
                self.eip += 2
                return "output"

            elif bop == 5: # JT
                a, b = get_params(self.ops, self.eip, self.base, 2)

                if a != 0:
                    self.eip = b
                else:
                    self.eip += 3

            elif bop == 6: # JF
                a, b = get_params(self.ops, self.eip, self.base, 2)

                if a == 0:
                    self.eip = b
                else:
                    self.eip += 3

            elif bop == 7: # LT
                a, b, dst = get_params(self.ops, self.eip, self.base, 3, last_dst=True)
                self.ops[dst] = int(a < b)
                self.eip += 4

            elif bop == 8: # EQ
                a, b, dst = get_params(self.ops, self.eip, self.base, 3, last_dst=True)
                self.ops[dst] = int(a == b)
                self.eip += 4

            elif bop == 9: # BASE
                a, = get_params(self.ops, self.eip, self.base, 1)
                self.base += a
                self.eip += 2

            elif bop == 99:
                return "exit"
            else:
                raise Exception("Unkown op: {}".format(op))

    
def solve(s):
    codes = [int(x) for x in s.split(",")]

    N = 50

    ms = [IntCode(codes[:]) for _ in range(N)]

    # Put in network ids
    for i, m in enumerate(ms):
        m.inputs.append(i)

    l_nat_x, l_nat_y = -1, -1
    nat_x, nat_y = 0, 0


    buffs = [[] for _ in range(N)]
    
    nat_last = None
    nat = None
    while True:
        idle = True
        for i, m in enumerate(ms):
            k = m.run()

            if k == "input":
                if buffs[i]:
                    idle = False
                    x, y = buffs[i].pop(0)
                    m.inputs.append(x)
                    m.inputs.append(y)
                else:
                    m.inputs.append(-1)
            elif k == "output":
                idle = False
                while 3 <= len(m.outputs):
                    dst = m.outputs.pop(0)
                    x = m.outputs.pop(0)
                    y = m.outputs.pop(0)

                    if dst == 255:
                        nat_last = nat
                        nat = (x,y)
                    else:
                        buffs[dst].append((x,y))
            else:
                print("WHAT?")

        if idle and nat:
            print("We have a nat: {}".format(nat))
            if nat_last and nat_last[1] == nat[1]:
                print("And the answer is: {}".format(nat[1]))
            elif not nat_last:
                print("The first nat is: {}".format(nat[1]))
            else:
                print("We got nat {} and the lat one was: {}".format(nat, nat_last))

            buffs[0].append(nat)
                


for line in fileinput.input():
    print(solve(line.strip()))
