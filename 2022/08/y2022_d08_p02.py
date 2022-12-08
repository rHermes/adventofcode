import fileinput as fi
import itertools as it

lines = filter(bool,map(str.rstrip,fi.input()))
grid = [[int(c) for c in line] for line in lines]
MY, MX = (len(grid), len(grid[0]))

def scene_score_f(ty, tx):
    h = grid[ty][tx]

    # up
    up_score = 0
    for y in reversed(range(ty)):
        up_score += 1
        if h <= grid[y][tx]:
            break
    # down
    down_score = 0
    for y in range(ty+1,MY):
        down_score += 1
        if h <= grid[y][tx]:
            break

    #left
    left_score = 0
    for x in reversed(range(tx)):
        left_score += 1
        if h <= grid[ty][x]:
            break

    # right
    right_score = 0
    for x in range(tx+1,MX):
        right_score += 1
        if h <= grid[ty][x]:
            break

    return right_score * left_score * up_score * down_score

# We simply apply the function to all interior spots. The reason for
# this is that the outer ones all have a 0 spot, and so cannot be anything
# but 0, since we multiple all directions together.
all_spots = it.product(range(1,MY-1), range(1,MX-1))
all_scores = it.starmap(scene_score_f, all_spots)

# incase we have a 2x2 map, where there are no interior spaces
ans = max(all_scores, default=0)
print(ans)
