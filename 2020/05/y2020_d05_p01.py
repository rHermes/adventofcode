import fileinput

# The list is of true, meaning upper, and false meaning lower.
def bsp(a):
    s = [0, 2**len(a) - 1]
    for d in a:
        s[not d] = (s[0] + s[1]) // 2 + d

    return s[0]

def pass_to_id(p):
    b = [x in 'BR' for x in p]
    return bsp(b[:7])*8 + bsp(b[7:10])
    
print(max(map(pass_to_id, fileinput.input())))
