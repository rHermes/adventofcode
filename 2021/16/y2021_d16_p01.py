import fileinput as fi

# inspired heavily by: https://old.reddit.com/r/adventofcode/comments/rhj2hm/2021_day_16_solutions/hoqwhnj/
# The idea here is that we never need to backtrack, so we can simply operate on one array. We reverse it,
# to get constant time `pop`.

def read_bits(data, n):
    for _ in range(n):
        yield data.pop()

def as_num(bits):
    return sum((2**i) * b for i, b in enumerate(reversed(bits)))

def read_num(data, n):
    return as_num(list(read_bits(data, n)))

def decode(data):
    """evaluate a treestructure"""
    version = read_num(data, 3)
    type_id = read_num(data, 3)

    def get_subpackets():
        if type_id == 4:
            while True:
                done = not data.pop()
                read_num(data, 4)
                if done:
                    return

        lid = data.pop()
        if lid:
            for _ in range(read_num(data, 11)):
                yield decode(data)
        else:
            blen = read_num(data, 15)
            l1 = len(data) - blen
            while len(data) != l1:
                yield decode(data)

    return version + sum(get_subpackets())


line = next(fi.input()).rstrip()
h = "".join("{:04b}".format(int(x, 16)) for x in line)
bits = [x == "1" for x in h][::-1]
print(decode(bits))
