import fileinput as fi
import collections as cs


# Input parsing
lines = [line.rstrip() for line in fi.input() if line != "\n"]

idx = 0
current_dir = ("root",)
dir_sizes = cs.defaultdict(int)
while idx < len(lines):
    parts = lines[idx].split(" ")
    idx += 1
    if parts[1] == "cd":
        if parts[2] == "/":
            current_dir = ("root",)
        elif parts[2] == "..":
            current_dir = current_dir[:-1]
        else:
            current_dir = current_dir + (parts[2],)
    else:
        # We must now consume an ls command
        while idx < len(lines) and not lines[idx].startswith("$ "):
            size, name = lines[idx].split(" ")
            idx += 1
            if size == "dir":
                continue
           
            
            size = int(size)
            for j in range(len(current_dir)):
                dir_name = "/".join(current_dir[:j+1])
                dir_sizes[dir_name] += size

ans = 0
for total_size in dir_sizes.values():
    if 100000 < total_size:
        continue
    ans += total_size

print(ans)
