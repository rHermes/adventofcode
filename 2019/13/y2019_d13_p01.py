import fileinput

def solve(s):
    codes = [int(x) for x in s.split(",")]
    # 387 is where the number of blocks are stored
    return codes[387]

for line in fileinput.input():
    print(solve(line.strip()))
