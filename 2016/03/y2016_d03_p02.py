import fileinput


n = 0
nums = [int(x) for line in fileinput.input() for x in line.rstrip().split()]

for i in range(0,len(nums),9):
    for j in range(3):
        # Using stride notation here
        a, b, c = sorted(nums[(i+j):(i+j)+7:3])
        if a + b > c:
            n += 1

print(n)
