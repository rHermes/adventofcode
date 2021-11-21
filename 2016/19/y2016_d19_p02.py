import fileinput as fi
import collections

# This was a fast ish solution that I was clued into by the reddit thread.
# It uses two deques to keep track of who to remove from the circle.
def stack_solve(n):
    left = collections.deque(range(1, n//2 + 1))
    right = collections.deque(range(n, n//2, -1))

    while left and right:
        if len(right) < len(left):
            left.pop()
        else:
            right.pop()

        # Rotate
        right.appendleft(left.popleft())
        left.append(right.pop())


    if left:
        return left[0]
    else:
        return right[0]


# This was created by looking at the output and spotting a pattern.
def smart_solve(N):
    largest = 1
    current = 1
    step = 1

    while step < N:
        step += 1

        if current < largest:
            current += 1
        elif current + 2 <= step:
            current += 2
            largest = current
        else:
            current = 1

    return current


print(smart_solve(int(next(fi.input()))))
