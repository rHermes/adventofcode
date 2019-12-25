import fileinput
from collections import defaultdict,  deque
from itertools import chain, combinations

def powerset(iterable):
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    """
    xs = list(iterable)
    # note we return an iterator rather than a list
    return chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1))

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



def route_to(G, src, dst):
    if src == dst:
        return []

    Q = deque([src])
    before = {}
    seen = set([src])

    while Q:
        v = Q.popleft()

        if v == dst:
            # We did it
            pth = [dst]
            dirs = []
            while pth[0] in before:
                d, u = before[pth[0]]
                dirs.insert(0, d)
                pth.insert(0, u)

            return dirs



        for d, u in G[v].items():
            if u in seen:
                continue

            before[u] = (d, v)
            seen.add(u)
            Q.append(u)

            




    
def solve(s):
    codes = [int(x) for x in s.split(",")]

    ic = IntCode(codes[:])

    
    buf_out = ""
    
    rooms = []

    
    node_id = 0
    next_node_id = 1
    G = defaultdict(dict)
    cur_path = []

    revdir = {"N": "S", "E": "W", "S": "N", "W": "E"}
    shorttolong = {"N": "north", "E": "east", "S": "south", "W": "west"}
    blacklist = ["photons", "giant electromagnet", "escape pod", "molten lava", "infinite loop"]

    sec_room_dir = ""

        
    FIRST = True
    Q = deque([0])
    seen = set()
    seen.add(node_id)


    rooms = {}
    inv = [] 

    while Q:
        v = Q.pop()
        
        path = route_to(G, node_id, v)
        #print("From {} to {}: {}".format(node_id, v, path))

        for st in path[:-1]:
            ic.inputs.extend(ord(c) for c in shorttolong[st] + "\n")

        # Now we run that

        while ic.run() == "output":
            while ic.outputs:
                buf_out += chr(ic.outputs.pop(0))

        assert(ic.run() == "input")

        for st in path[-1:]:
            ic.inputs.extend(ord(c) for c in shorttolong[st] + "\n")
        
        if not FIRST:
            buf_out = ""
        else:
            FIRST = False

        while ic.run() == "output":
            while ic.outputs:
                buf_out += chr(ic.outputs.pop(0))

        node_id = v

        assert(ic.run() == "input")


        lines = buf_out.splitlines()
#        print(lines)
        buf_out = ""

        name = lines[3]
        desc = lines[4]

        # Items
        items = []
        if 'Items here:' in lines:
            stx = lines.index('Items here:') + 1
            edx = lines.index('', stx+1)
            items = [s[2:] for s in lines[stx:edx]]
            for item in items:
                if item not in blacklist:
                    ic.inputs.extend(ord(c) for c in "take {}\n".format(item))
                    inv.append(item)

            # I'm going to take all these
#            print("We are picking up: {}".format(items))
            while ic.run() == "output":
                while ic.outputs:
                    buf_out += chr(ic.outputs.pop(0))
            buf_out = ""
            assert(ic.run() == "input")
            

        rooms[node_id] = (name, desc, items)
       #  print(name, desc, items)

        idx = lines.index('Doors here lead:') + 1
        edx = lines.index('', idx)

        dirs = [s[2].upper() for s in lines[idx:edx]]
        
        # We don't need this one

        for d in dirs:
            if d not in G[node_id]:
                G[node_id][d] = next_node_id
                G[next_node_id][revdir[d]] = node_id
                next_node_id += 1

            if G[node_id][d] not in seen:
                if name == "== Security Checkpoint ==":
                    sec_room_dir = d
                else:
                    seen.add(G[node_id][d])
                    Q.append(G[node_id][d])


    robot_node_id = node_id

    for node_id, (name, desc, items) in rooms.items():
        if name == "== Security Checkpoint ==":
            security_room_id = node_id
            break

    path = route_to(G, robot_node_id, security_room_id)
    for st in path:
        ic.inputs.extend(ord(c) for c in shorttolong[st] + "\n")

    while ic.run() == "output":
        while ic.outputs:
            buf_out += chr(ic.outputs.pop(0))
    buf_out = ""
    assert(ic.run() == "input")
    
    all_items = inv[:]
    sinv = set(inv)

    TOO_HEAVY = 'A loud, robotic voice says "Alert! Droids on this ship are lighter than the detected value!" and you are ejected back to the checkpoint.'
    TOO_LIGHT = 'A loud, robotic voice says "Alert! Droids on this ship are heavier than the detected value!" and you are ejected back to the checkpoint.'
    # First we drop all the items and then we collect them all again
    for itemcomb in powerset(all_items):
        sdst = set(itemcomb)

        need_to_pick_up = sdst - sinv
        need_to_drop = sinv - sdst
        sinv = sdst

        # We drop what we need to drop
        for i in need_to_drop:
            ic.inputs.extend(ord(c) for c in "drop {}\n".format(i))
        # We pick up what we need
        for i in need_to_pick_up:
            ic.inputs.extend(ord(c) for c in "take {}\n".format(i))
        while ic.run() == "output":
            while ic.outputs:
                buf_out += chr(ic.outputs.pop(0))
        buf_out = ""
        assert(ic.run() == "input")

        ic.inputs.extend(ord(c) for c in shorttolong[sec_room_dir] + "\n")
        while ic.run() == "output":
            while ic.outputs:
                buf_out += chr(ic.outputs.pop(0))

        lines = buf_out.splitlines()
        buf_out = ""
        weight = 0
        for line in lines:
            if line == TOO_LIGHT:
                weight = -1
            elif line == TOO_HEAVY:
                weight = 1

        if weight == 0:
            return lines[-1].split(" ")[11]

        assert(ic.run() == "input")


for line in fileinput.input():
    print(solve(line.strip()))
