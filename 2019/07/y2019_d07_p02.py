import fileinput
import itertools as it
import threading
import queue

def exec(ops, input_queue, output_queue):
    eip = 0
    while True:
        op = ops[eip]
        bop = op % 100
        
        if bop == 1: # ADD 
            a = ops[eip+1]
            b = ops[eip+2]
            dst = ops[eip+3]
            if op == 1:
                ops[dst] = ops[a] + ops[b]
            elif op == 1_01:
                ops[dst] = a + ops[b]
            elif op == 10_01:
                ops[dst] = ops[a] + b 
            elif op == 11_01:
                ops[dst] = a + b
            else:
                raise Exception("Not valid instruction!")

            eip += 4

        elif bop == 2: # MULT
            a = ops[eip+1]
            b = ops[eip+2]
            dst = ops[eip+3]
            if op == 2:
                ops[dst] = ops[a] * ops[b]
            elif op == 1_02:
                ops[dst] = a * ops[b]
            elif op == 10_02:
                ops[dst] = ops[a] * b 
            elif op == 11_02:
                ops[dst] = a * b
            else:
                raise Exception("Not valid instruction!")

            eip += 4

        elif bop == 3: # INPUT
            dst = ops[eip+1]

            # We are faking the in
            ins = input_queue.get()

            if op == 3:
                ops[dst] = ins
            else:
                raise Exception("Not valid input!")

            eip += 2
        
        elif bop == 4: # OUTPUT
            src = ops[eip+1]
            
            if op == 4:
                output_queue.put(ops[src])
            elif op == 1_04:
                output_queue.put(src)
            else:
                raise Exception("not valid output!")
        
            eip += 2

        elif bop == 5: # JT
            a = ops[eip+1]
            b = ops[eip+2]

            test_val = 0
            test_dst = 0
            if op == 5:
                test_val = ops[a]
                test_dst = ops[b]
            elif op == 1_05:
                test_val = a
                test_dst = ops[b]
            elif op == 10_05:
                test_val = ops[a]
                test_dst = b
            elif op == 11_05:
                test_val = a
                test_dst = b
            else:
                raise Exception("Not a valid JT")

            if test_val != 0:
                eip = test_dst
            else:
                eip += 3

        elif bop == 6: # JF
            a = ops[eip+1]
            b = ops[eip+2]

            test_val = 0
            test_dst = 0
            if op == 6:
                test_val = ops[a]
                test_dst = ops[b]
            elif op == 1_06:
                test_val = a
                test_dst = ops[b]
            elif op == 10_06:
                test_val = ops[a]
                test_dst = b
            elif op == 11_06:
                test_val = a
                test_dst = b
            else:
                raise Exception("Not a valid JF")

            if test_val == 0:
                eip = test_dst
            else:
                eip += 3

        elif bop == 7: # LT
            a = ops[eip+1]
            b = ops[eip+2]
            dst = ops[eip+3]
            if op == 7:
                ops[dst] = int(ops[a] < ops[b])
            elif op == 1_07:
                ops[dst] = int(a < ops[b])
            elif op == 10_07:
                ops[dst] = int(ops[a] < b)
            elif op == 11_07:
                ops[dst] = int(a < b)
            else:
                raise Exception("Not a valid LT!")

            eip += 4

        elif bop == 8: # EQ
            a = ops[eip+1]
            b = ops[eip+2]
            dst = ops[eip+3]
            if op == 8:
                ops[dst] = int(ops[a] == ops[b])
            elif op == 1_08:
                ops[dst] = int(a == ops[b])
            elif op == 10_08:
                ops[dst] = int(ops[a] == b)
            elif op == 11_08:
                ops[dst] = int(a == b)
            else:
                raise Exception("Not a valid EQ!")

            eip += 4
        elif bop == 99:
            break
        else:
            raise Exception("Unkown op: {}".format(op))


def solve(s):
    ops = [int(x) for x in s.split(",")]
    makis = 0
    for per in it.permutations([5, 6, 7, 8, 9]):
        threads = []
        q1 = queue.Queue()
        q2 = queue.Queue()
        q3 = queue.Queue()
        q4 = queue.Queue()
        q5 = queue.Queue()
        
        threads.append(threading.Thread(target=exec, args=(ops[:], q1, q2)))
        threads.append(threading.Thread(target=exec, args=(ops[:], q2, q3)))
        threads.append(threading.Thread(target=exec, args=(ops[:], q3, q4)))
        threads.append(threading.Thread(target=exec, args=(ops[:], q4, q5)))
        threads.append(threading.Thread(target=exec, args=(ops[:], q5, q1)))

        for t in threads:
            t.start()

        q1.put(per[0])
        q2.put(per[1])
        q3.put(per[2])
        q4.put(per[3])
        q5.put(per[4])

        q1.put(0)

        for t in threads:
            t.join()

        ins = q1.get()

        if ins > makis:
            makis = ins

    return makis 

for line in fileinput.input():
    print(solve(line.strip()))
