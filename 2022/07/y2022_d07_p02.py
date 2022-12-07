import fileinput as fi
import collections as cs
import graphlib


# Input parsing
lines = [line.rstrip() for line in fi.input() if line != "\n"]

G = graphlib.TopologicalSorter()


files = set()
node_sizes = cs.defaultdict(int)


current_dir = ("root",)
idx = 0
while idx < len(lines):
    parts = lines[idx].split(" ")
    idx += 1
    if parts[1] == "cd":
        if parts[2] == "/":
            current_dir = ("root",)
        elif parts[2] == "..":
            current_dir = current_dir[:-1]
        else:
            new_dir = current_dir + (parts[2],)
            G.add(current_dir, new_dir)
            current_dir = new_dir
    else:
        # We must now consume an ls command
        while idx < len(lines) and not lines[idx].startswith("$ "):
            size, name = lines[idx].split(" ")
            idx += 1
            if size == "dir":
                continue
           
            size = int(size)
            filename = current_dir + (name,)
            files.add(filename)

            node_sizes[filename] = size

            G.add(current_dir, filename)

# We now add together all the nodes, from the bottom up
for node in G.static_order():
    if node == ("root",):
        continue

    base = node[:-1]
    node_sizes[base] += node_sizes[node]


# Find the answer.
root_cost = node_sizes[("root",)]
current = 70000000 - root_cost
needed = 30000000
minimal = needed - current

for node, total_size in sorted(node_sizes.items(), key=lambda xs: xs[1]):
    if minimal <= total_size and node not in files:
        print(total_size)
        break
