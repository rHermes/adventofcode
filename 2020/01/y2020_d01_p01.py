import fileinput

nums = []
for line in fileinput.input():
    nums.append(int(line.rstrip()))

for x in range(len(nums)):
    for y in range(x,len(nums)):
        if nums[x]+nums[y] == 2020:
            print(nums[x]*nums[y])
