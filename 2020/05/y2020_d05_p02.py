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
                
    return (s[0], k[0]) 

def seat_to_id(s):
    return s[0]*8 + s[1]

ans = 0
passes = [line.rstrip() for line in fileinput.input()]

places = set()
ids = set()
for x in range(128):
    for y in range(8):
        places.add((x,y))


for p in passes:
    s = pass_to_seat(p)
    places.remove(s)
    ids.add(seat_to_id(s))

for s in places:
    i = seat_to_id(s)
    if i+1 in ids and i-1 in ids:
        print(s, i)
