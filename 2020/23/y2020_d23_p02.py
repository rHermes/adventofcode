import fileinput as fi

def solve(cups, moves=100, pad=1_000_000):
    N = max(len(cups),pad)

    A = [(i+1)%N for i in range(N)]
    for i,x in enumerate(cups[:-1]):
        A[x-1] = cups[(i+1)]-1

    if len(cups):
        A[cups[-1]-1] = len(cups)
        A[-1] = cups[0]-1

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

    return (A[0]+1)*(A[A[0]]+1)

cups = [int(x) for x in "".join(fi.input()).rstrip()]
print(solve(cups, moves=10_000_000))
