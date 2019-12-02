import fileinput

def solve(ops):
    
    eip = 0
    while ops[eip] != 99:
        op = ops[eip]
        a = ops[eip+1]
        b = ops[eip+2]
        dst = ops[eip+3]
        if op == 1:
            ops[dst] = ops[a] + ops[b]
        if op == 2:
            ops[dst] = ops[a] * ops[b]

        eip += 4

    return ops

def real_solve(ops):
    for noun in range(100):
        for verb in range(100):
            ops[1] = noun
            ops[2] = verb
            com = solve(ops.copy())
            if com[0] == 19690720:
                print("Noun: {}, Verb: {}".format(noun, verb))
                return 100*noun + verb

test_cases = [
        ([1,0,0,0,99],  [2,0,0,0,99]),
        ([2,3,0,3,99],  [2,3,0,6,99]),
        ([2,3,0,3,99],  [2,3,0,6,99]),
        ([2,4,4,5,99,0], [2,4,4,5,99,9801]),
        ([1,1,1,4,99,5,6,0,99], [30,1,1,4,2,5,6,0,99])
        ]

for t, e in test_cases:
    com = solve(t)
    if com != e:
        print("Expected {} for {}, but got {}".format(e, t, com))

for line in fileinput.input():
    ops = [int(x) for x in line.strip().split(",")]
    ans = real_solve(ops)
    print(ans)
