import fileinput


n = 0
for line in fileinput.input():
    nums = [int(x) for x in line.rstrip().split()]
    a, b, c = sorted(nums)
    if a + b > c:
        n += 1

print(n)
