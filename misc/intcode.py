"""
Obeservations:

The base is really a stack of sorts

Call convention for a function with N args
m[base + n] = arg (N - n)
m[base + 0] = return addres

return value is in m[base + 1] when address returns

m[base - n] is the nth arg in a function

functions start with adding N + 1 to the base and popit of before returning

GENERAL:

since variable memory locations is not allowed, the only way to write to a
dynamic place in memory is to modify the code in the instruction that does the load,
more specifically, the destination
"""

code2name = {
    1: "ADD",
    2: "MULT",
    3: "INPUT",
    4: "OUTPUT",
    5: "JT",
    6: "JF",
    7: "LT",
    8: "EQ",
    9: "BASE",
    99: "HALT"
        }

class Op:
    def __init__(self, place, code, args):
        self.place = place
        self.code = code
        self.args = args

class Arg:
    def __init__(self,val,t,desc=""):
        self.val = val
        self.t = t
        self.desc = desc

def get_param_type(op, nargs):
    ddd = ("{:0" + str(nargs+2) + "}").format(op)
    return list(reversed([int(x) for x in ddd[:-2]]))

def get_args(ops, ip, nargs):
    op = ops[ip]
    tps = get_param_type(op, nargs)
    args = []
    for i, t in enumerate(tps):
        a = Arg(ops[ip+1+i], t)
        args.append(a)
    
    return args


# Ops is a list of ints
def disass(ops, ip=0):
    dis = [] 
    while ip < len(ops):
        op = ops[ip]
        bop = op % 100

        if bop not in code2name:
            ip += 1
            continue

        if bop == 1: # ADD
            a, b, dst = get_args(ops, ip, 3)
            o = Op(ip, op, [a,b,dst])
        elif bop == 2: # MULT
            a, b, dst = get_args(ops, ip, 3)
            o = Op(ip, op, [a,b,dst])
        elif bop == 3: # INPUT
            dst, = get_args(ops, ip, 1)
            o = Op(ip, op, [dst])
        elif bop == 4: # OUTPUT
            src, = get_args(ops, ip, 1)
            o = Op(ip, op, [src])
        elif bop == 5: # JT
            a, b = get_args(ops, ip, 2)
            o = Op(ip, op, [a, b])
        elif bop == 6: # JF
            a, b = get_args(ops, ip, 2)
            o = Op(ip, op, [a, b])
        elif bop == 7: # LT
            a, b, dst = get_args(ops, ip, 3)
            o = Op(ip, op, [a,b,dst])
        elif bop == 8: # EQ
            a, b, dst = get_args(ops, ip, 3)
            o = Op(ip, op, [a,b,dst])
        elif bop == 9: # BASE
            a, = get_args(ops, ip, 1)
            o = Op(ip, op, [a])
        elif bop == 99: # HALT
            o = Op(ip, op, [])
        else:
            raise Exception("This should never happen")

        dis.append(o)
        ip += len(o.args) + 1

    return dis


def print_disas(dis):
    fmt = "{:10}: {:10} {:6} {}"
    for d in dis:
        argss = []
        for a in d.args:
            if a.t == 2:
                argss.append("m[base + {}]".format(a.val))
            elif a.t == 1:
                argss.append("{}".format(a.val))
            elif a.t == 0:
                argss.append("m[{}]".format(a.val))
            else:
                raise Exception("This should never happend, invalid arg type")
        
        arg_str = ", ".join(argss)

        print(fmt.format(d.place, d.code, code2name[d.code % 100], arg_str))


def read_in_ops(fp):
    with open(fp, "r") as f:
        wow = f.read()

    wow = wow.strip()
    codes = [int(x) for x in wow.split(",")]
    return codes
