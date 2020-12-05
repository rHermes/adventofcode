import fileinput


def pass_to_seat(p):
    s = [0, 127]
    for c in p[:7]:
        if c == 'F':
            s[1] = (s[0] + s[1]) // 2
        elif c == 'B':
            s[0] = (s[0] + s[1]) // 2 + 1
        else:
            raise Exception("WTF")


    assert(s[0] == s[1])

    k = [0, 7]
    for c in p[7:]:
        if c == 'L':
            k[1] = (k[0] + k[1]) // 2
        elif c == 'R':
            k[0] = (k[0] + k[1]) // 2 + 1
        else:
            raise Exception("WTF")
    
    assert(k[0] == k[1])
                
    # return (s[0], k[0]) 
    return s[0]*8 + k[0] 

ans = 0
passes = [line.rstrip() for line in fileinput.input()]

print(max(map(pass_to_seat, passes)))
# for p in passes:
#     print("{}: {}".format(p, pass_to_seat(p)))


