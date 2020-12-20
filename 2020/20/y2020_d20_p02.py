import fileinput as fi
import itertools as it
import functools as ft
import numpy as np
import collections


def parse_input(INPUT):
    IN = None
    images = {}
    groups = INPUT.split("\n\n")
    for grp in INPUT.split("\n\n"):
        # print(grp)
        lins = list(grp.splitlines())
        tid = int(lins[0][5:-1])
        img = np.array([[x == '#' for x in line] for line in lins[1:]])
        if IN == None:
            IN = len(img[0])
        images[tid] = img

    PN = int(len(images)**(0.5))

    return (PN,IN,images)


def morph_image(image, ud, rot):
    M = image
    if ud:
        M = np.flipud(M)

    return np.rot90(M,-rot)

def get_side(image, side):
    if side == 0:
        return image[0]
    elif side == 1:
        return image[:,-1]
    elif side == 2:
        return image[-1]
    elif side == 3:
        return image[:,0]
    else:
        raise "invalid side given!"

# yields all possible versions of an image
def generate_permutations(image):
    for flipud in [False, True]:
        for rot in [0,1,2,3]:
            yield (flipud, rot, morph_image(image, flipud, rot))

def print_image(image):
    for v in image:
        for vv in v:
            if vv:
                print("#", end="")
            else:
                print(".", end="")
        print("")

# prints just the ids or print the board too
def print_board(images, board, ids=True):
    assert(ids == True)

    for y in board:
        for x in y:
            if x:
                print("{} ".format(x[2]), end="")
            else:
                print("XXXX ", end="")
        print("")
        # for ud, rot, tid in y:
        #     print()




# Takes in an image, an iterator of others, and a side to compare against.
# This will return the number of items which match that side.
# Takes the images, our id and a set of other ids
def check_side(images, image, others, side):
    s = get_side(image, side)
    ans = []
    for oid in others:
        for ud,rot,perm in generate_permutations(images[oid]):
            o = get_side(perm, (side+2)%4)
            if (s == o).all():
                ans.append((ud,rot,oid))

    return ans


def check_sides(images, image, others):
    ans = [[],[],[],[]]
    for oid in others:
        for ud,rot,perm in generate_permutations(images[oid]):
            for side in [0,1,2,3]:
                s = get_side(image, side)
                o = get_side(perm, (side+2)%4)
                if (s == o).all():
                    ans[side].append((ud,rot,oid))

    return ans

# This find the borders pieces in the pile
def find_borders(images, pile):
    corners = set()
    borders = set()
    for tid in pile:
        sides = check_sides(images, images[tid], ids - set((tid,)))
        matches = sum(len(x) == 0 for x in sides)
        if matches == 2:
            corners.add(tid)
        if matches == 1:
            borders.add(tid)

    # We return the corners and borders
    return (corners, borders)

# Builds the entire picture frame, and returns it as an array
# of the rotations and such of the picture
def build_frame(images, corners, borders):
    # We just pick the corner with the least value
    start_corner = min(corners)
    # print("We will start with {} in the upper left corner".format(start_corner))
    PN = len(borders)//4 + 2
    board = [[None for _ in range(PN)] for _ in range(PN)]

    # Now we place the first piece, orienting it so that it's done
    for ud, rot, perm in generate_permutations(images[start_corner]):
        north, east, south, west = check_sides(images, perm, borders - set([start_corner]))
        if len(north) == 0 and len(west) == 0:
            assert(len(east) == 1)
            assert(len(south) == 1)
            break
    else:
        raise "Not valid orientation found" 

    # These are the ids that are taken
    taken = set([start_corner, east[0][2], south[0][2]])

    # We fill in the ones we know
    board[0][0] = (ud, rot, start_corner)
    board[0][1] = east[0]
    board[1][0] = south[0]

    # Now to simply build the rest of the picture,
    # assuming that there is only one 
    frontier = collections.deque([(0,1), (1,0)])
    while frontier:
        py,px = frontier.pop()
        pud, prot, pid = board[py][px]
        pimg = morph_image(images[pid], pud, prot)
        # print("We are processing ({},{}) which has id {}".format(px,py, pid))

        north, east, south, west = check_sides(images, pimg, (borders | corners) - taken)
        assert(all(len(x) in [0,1] for x in [north, east, south, west]))

        if north:
            tmp = north[0]
            board[py-1][px] = tmp
            frontier.appendleft((py-1,px))
            taken.add(tmp[2])

        if east:
            tmp = east[0]
            board[py][px+1] = tmp
            frontier.appendleft((py,px+1))
            taken.add(tmp[2])

        if south:
            tmp = south[0]
            board[py+1][px] = tmp
            frontier.appendleft((py+1,px))
            taken.add(tmp[2])

        if west:
            tmp = west[0]
            board[py][px-1] = tmp
            frontier.appendleft((py,px-1))
            taken.add(tmp[2])

        # assert(sum(len(x) == ))

    return board


# This fills the frame, starting at 
def fill_frame(images, board, pile, taken):
    PN = len(borders)//4 + 2
    board = board.copy()

    # We fill the puzzle from upper left corner always going up and down
    py, px = 1, 1
    while not board[py][px]:
        # print("We are checking out ({},{})".format(px,py))
        # Check above us
        # print(board)
        nud, nrot, nid = board[py-1][px]
        nimg = morph_image(images[nid], nud, nrot)

        ns = check_side(images, nimg, pile - taken, 2)
        assert(len(ns) == 1)
        board[py][px] = ns[0]
        taken.add(ns[0][2])


        # break
        # move on to the next cell
        if board[py+1][px]:
            py, px = 1, px + 1
        else:
            py += 1

# Returns the positions of an offset x
def get_dragon_pos():
    dragon = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   ",
    ]
    pos = []
    for y, row in enumerate(dragon):
        for x, c in enumerate(row):
            if c == "#":
                pos.append([y,x])

    return np.array(pos)


def build_image(images, board):
    act = [
        [morph_image(images[tid], ud, rot)[1:-1,1:-1] for ud,rot,tid in row]
        for row in board
    ]
    return np.block(act)

def find_dragons(pic):
    ROWS, COLS = pic.shape
    pos = get_dragon_pos()
    mx = pos[0][1]+2
    dragon_pos = []
    for y in range(ROWS-3):
        for x in range(COLS-mx):
            if pic[y + pos[:,0], x + pos[:,1]].all():
                dragon_pos.append((y,x))


    return dragon_pos


def water_roughness(pic, dragons):
    pos = get_dragon_pos()
    for dy,dx in dragons:
        pic[dy + pos[:,0], dx + pos[:,1]] = False

    return np.sum(pic)


INPUT = "".join(fi.input())
(PN,IN,images) = parse_input(INPUT)

# print("The grid of images is {0}x{0}".format(PN))
# print("An image is {0}x{0}".format(IN))

ids = set(images.keys())

# We cheat here to make experimentation a bit faster
corners, borders = find_borders(images, ids)

# print("CORNERS:",corners)
# print("BORDERS:",borders)

board = build_frame(images, corners, borders)
# print_board(images, board)
fill_frame(images,board, ids, corners | borders)
# print("")
# print_board(images, board)

img = build_image(images, board)
for ud, rot, perm in generate_permutations(img):
    dragons = find_dragons(perm)
    if dragons:
        # print(dragons)
        print(water_roughness(perm, dragons))
