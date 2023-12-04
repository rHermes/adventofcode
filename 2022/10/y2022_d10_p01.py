import fileinput as fi

def get_instructions():
    for line in filter(bool, map(str.rstrip, fi.input())):
        if line.startswith("addx "):
            yield "noop"

        yield line


def solve():
    reg = 1
    ans = 0
    
    # We start at 2, as that is, as the cylce here, is the one more
    # than the current cycle we are on, and we would normally start on 1
    for cycle, inst in enumerate(get_instructions(), start=2):
        parts = inst.split(" ")
        if parts[0] == "addx":
            reg += int(parts[1])

        if 20 <= cycle and (cycle - 20) % 40 == 0:
            ans += cycle * reg

    return ans

print(solve())
