import fileinput as fi

# The trick in this one, is that we can always just set the
# tail to the last position of the head. The head cannot move
# diagonally, so we will always move to the place it was last.

DIRS = {"D": -1j, "R": 1, "L": -1, "U": 1j}

head = 0
tail = 0
visited = {0}

lines = filter(bool, map(str.rstrip, fi.input()))

for line in lines:
    dir, amount = line.split(" ")
    odelta  = DIRS[dir]
    amount = int(amount)
    for _ in range(amount):
        new_head = head + odelta
        if 2 <= abs(new_head - tail):
            tail = head
            visited.add(tail)

        head = new_head

print(len(visited))
