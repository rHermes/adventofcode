import fileinput as fi
import regex

# Prepare a lookup table
nums = "123456789"
dec_nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
vals = {k: int(k) for k in nums}

reg = "|".join(list(nums) + dec_nums)

for i, dnum in enumerate(dec_nums, start=1):
    vals[dnum] = i
   
ans = 0
for line in map(str.rstrip, fi.input()):
    hits = regex.findall(reg, line, overlapped=True)
    ans += 10*vals[hits[0]] + vals[hits[-1]]

print(ans) 
