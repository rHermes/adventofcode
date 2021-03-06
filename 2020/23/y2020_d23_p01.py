import fileinput as fi

def solve(cups, moves=100):
    N = len(cups)
    A = [0 for i in range(N)]
    for i,x in enumerate(cups):
        A[x-1] = cups[(i+1)%N]-1

    cur = cups[0]-1
    for move in range(moves):
        a = A[cur]
        b = A[a]
        c = A[b]

        # Find the first number not in our numbers
        dst = (cur-1) % N
        while dst in [cur,a,b,c]:
            dst = (dst-1) % N

        # Update the linked list
        A[cur] = A[c]
        A[c] = A[dst]
        A[dst] = a

        cur = A[cur]

    ans = ""
    cur = A[0]
    while cur != 0:
        ans += str(cur+1)
        cur = A[cur]
    return ans

cups = [int(x) for x in "".join(fi.input()).rstrip()]
print(solve(cups, moves=100))
