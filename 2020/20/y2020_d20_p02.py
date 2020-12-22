import fileinput as fi
import itertools as it
from collections import deque

def get_images():
    groups = "".join(fi.input()).split("\n\n")
    for group in groups:
        lines = group.splitlines()
        tid = int(lines[0][5:-1])
        img = [[x == '#' for x in line] for line in lines[1:]]
        yield (tid,img)

def reverse_bits(n, no_of_bits):
    """reverse bits in number"""
    result = 0
    for i in range(no_of_bits):
        result <<= 1
        result |= n & 1
        n >>= 1
    return result

def get_int_borders(image):
    BN = len(image)
    n = sum(image[0][i] << (BN-1-i) for i in range(BN))
    e = sum(image[i][BN-1] << (BN-1-i) for i in range(BN))
    s = sum(image[BN-1][i] << (BN-1-i) for i in range(BN))
    w = sum(image[i][0]  << (BN-1-i) for i in range(BN))
    return (n, e, s, w)

def rot_borders(borders, BN):
    """return the border rotated clockwise"""
    n,e,s,w = borders
    return (reverse_bits(w, BN), n, reverse_bits(e, BN), s)

def flip_borders(borders, BN):
    """returns the border flipped upside down"""
    n,e,s,w = borders
    return (s, reverse_bits(e, BN), n, reverse_bits(w, BN))

def morph_borders(borders, ud, rot, BN):
    """Returns a version of borders, which is rotated"""
    M = borders
    if ud:
        M = flip_borders(M, BN)

    for _ in range(rot):
        M = rot_borders(M, BN)

    return M


# This has been tested to make sure it's correct. DON'T TOUCH!
def orient(i, j, rev):
    """What rotation must we apply to get border i, to border j, rev is true if it must be reversed"""
    O = bool(i % 2)
    E = not O

    dst = (j - i) % 4
    if dst == 0:
        return (rev, rev*2*E)
    elif dst == 1:
        return (rev ^ O, 1 + 2*(rev and E))
    elif dst == 2:
        return (not rev, 2*(O or rev))
    elif dst == 3:
        return (rev ^ E, 3 - 2*(not rev and E))

def solve_puzzle(images):
    borders = {tid: get_int_borders(image) for tid, image in images.items()}
    PN = int(len(images)**(0.5))
    ids = list(borders.keys())


    pile = set(ids[1:])
    places = {(0,0): (ids[0], False, 0)}
    frontier = deque([(0,0)])
    BN = len(images[ids[0]])

    while frontier:
        px, py = frontier.popleft()
        pid, pud, prot = places[(px,py)]

        pborders = morph_borders(borders[pid], pud, prot, BN)
        for i, (dx,dy) in enumerate([(0,-1), (1,0), (0,1), (-1,0)]):
            spot = (px+dx,py+dy)
            if spot in places:
                continue

            pborder = pborders[i]
            rev_pborder = reverse_bits(pborder, BN)

            for tid in pile:
                tborders = borders[tid]

                for j, tborder in enumerate(tborders):
                    if tborder in [pborder, rev_pborder]:
                        mud, mrot = orient(j,(i+2)%4, tborder == rev_pborder)
                        pile.remove(tid)
                        places[spot] = (tid,mud,mrot)
                        frontier.append(spot)
                        break
                else:
                    continue

                break


    mx,my = min(places.keys())
    return [[places[(mx+dx,my+dy)] for dx in range(PN)] for dy in range(PN)]

def rotate_image(image):
    ans = [[] for _ in range(len(image))]
    for row in reversed(image):
        for i,c in enumerate(row):
            ans[i].append(c)

    return ans

def flip_image(image):
    return list(reversed(image))

def morph_image(image, up, rot):
    M = image
    if up:
        M = flip_image(M)
    for _ in range(rot):
        M = rotate_image(M)

    return M

def trim_image(image):
    return [x[1:-1] for x in image[1:-1]]

# Returns a 2d bool array
def create_picture(images, solved):
    PN = int(len(images)**(0.5))
    BN = len(next(iter(images.values())))

    pic = []
    for row in solved:
        prow = [[] for _ in range(BN-2)]

        for tid, ud, rot in row:
            image = morph_image(trim_image(images[tid]), ud, rot)
            for i, irow in enumerate(image):
                prow[i].extend(irow)

        pic.extend(prow)

    return pic

# Returns the positions of an offset x
def get_dragon_pos():
    dragon = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   ",
    ]
    pos = []
    mx = 0
    my = 0
    for y, row in enumerate(dragon):
        for x, c in enumerate(row):
            if c == "#":
                if mx < x:
                    mx = x
                my = y
                pos.append((y,x))

    return (pos,mx,my)


def find_dragons(pic):
    ROWS, COLS = len(pic), len(pic[0])
    (dd,MX,MY) = get_dragon_pos()
    dragon_pos = []
    for y in range(ROWS-MY):
        for x in range(COLS-MX):
            for dy, dx in dd:
                if not pic[y + dy][x + dx]:
                    break
            else:
                dragon_pos.append((y,x))

    return dragon_pos

def water_roughness(pic, dragons):
    dd, _, _ = get_dragon_pos()
    for y,x in dragons:
        for dy,dx in dd:
            pic[y+dy][x+dx] = False

    return sum(it.chain.from_iterable(pic))


images = dict(get_images())
solved = solve_puzzle(images)
picture = create_picture(images, solved)
for i in range(8):
    if i == 3:
        picture = flip_image(picture)

    dragons = find_dragons(picture)
    if dragons:
        print(water_roughness(picture, dragons))
        break

    picture = rotate_image(picture)
