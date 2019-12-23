import fileinput

# This is learned from the reddit thread about solutons:
#
# https://web.archive.org/web/20191223080504/https://old.reddit.com/r/adventofcode/comments/ee0rqi/2019_day_22_solutions/fbnkaju/

def solve(insts, N, R, pos):
    # We need to figure out what the offset and increment we have
    # between two rounds
    offset_diff = 0
    increment_mul = 1

    # We can cheat here and use euleres theorem since all our ns
    # will be prime, as they have to cover everything without overlap
    def inv(n):
        return pow(n, N-2, N)

    for inst in insts:
        if inst == "deal into new stack":
            increment_mul *= -1
            increment_mul %= N

            offset_diff += increment_mul
            offset_diff %= N
        elif inst.startswith("cut"):
            n = int(inst[3:])

            offset_diff += increment_mul * n
            offset_diff %= N

        elif inst.startswith("deal with increment"):
            n = int(inst[20:])

            increment_mul *= inv(n)
            increment_mul %= N
        else:
            raise Exception("Don't know inst: {}".format(inst))


    increment = pow(increment_mul, R, N)
    
    # this is based on a geometric series
    offset = offset_diff * (1 - increment) * inv(1 - increment_mul)
    offset %= N

    return (offset + increment*pos) % N


insts = [line.strip() for line in fileinput.input()]
print(solve(insts, 119315717514047, 101741582076661, 2020))
