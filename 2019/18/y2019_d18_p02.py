import fileinput
import collections
import itertools as it

Point =  collections.namedtuple('P', 'x y')

class Path():
    def __init__(self, current, collected_keys, length):
        self.current = current
        self.collected_keys = collected_keys
        self.length = length

    def get_state(self):
        unique_state = (self.current, self.collected_keys)
        return unique_state
    
    def path_length(self):
        return bin(self.collected_keys).count("1")
    
    def __repr__(self):
        return str(self.current) + " " + str(bin(self.collected_keys)) + " : " + str(self.length)

def route_to(G, src, dst):
    before = {}
    Q = collections.deque([src])
    seen = set([src])

    while len(Q) > 0:
        v = Q.popleft()

        if v == dst:
            # Here we found it. Now to construct a way back
            lst = [v]
            while lst[0] in before:
                lst.insert(0, before[lst[0]])

            return lst
        
        for u in G[v]:
            if u in seen:
                continue

            seen.add(u)
            before[u] = v
            Q.append(u)

    return None

def get_grid(part_b=False):
    grid = collections.defaultdict(int)
    keys = {}
    doors = {}
    start_points = []

    lines = [list(x.strip()) for x in fileinput.input()]
    mid_y = (len(lines) - 1) // 2
    mid_x = (len(lines[0]) - 1) // 2

    # if this is part B, we modify the middle
    if part_b:
        lines[mid_y-1][mid_x-1:mid_x+2] = "@#@"
        lines[mid_y][mid_x-1:mid_x+2] = "###"
        lines[mid_y+1][mid_x-1:mid_x+2] = "@#@"

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c != '#':
                p = Point(x, y)
                grid[p] = 1
                if c == '@':
                    start_points.append(p)
                elif c != '.':
                    o = ord(c)
                    if o >= ord("a"):
                        keys[o - ord("a")] = p
                    else:
                        doors[o - ord("A")] = p
    
    total_start_points = len(start_points)
    keys = {k + total_start_points : v for k, v in keys.items()}
    doors = {k + total_start_points : v for k, v in doors.items()}

    return grid, keys, doors, start_points, x, y

def get_surrounding_points(p):
    return set([
        Point(p.x, p.y-1),
        Point(p.x, p.y+1),
        Point(p.x-1, p.y),
        Point(p.x+1, p.y),
    ])

def build_graph(grid, max_x, max_y):
    G = collections.defaultdict(set)
    for x in range(max_x+1):
        for y in range(max_y+1):
            p = Point(x, y)
            if grid[p]:
                for sp in get_surrounding_points(p):
                    if grid[sp]:
                        G[p].add(sp)

    return G

#  Returns the distance and the doors in the way
def get_distance(G, p0, p1, doors):
    pp = route_to(G, p0, p1)
    if pp is None:
        return None

    # Now we must figure out which doors are in the way
    path_set = set(pp)
    doors_in_way = 0
    for k, p in doors.items():
        if p in path_set:
            doors_in_way += (1 << k)

    distance = len(pp) - 1
    return distance, doors_in_way



# This defines a matrix of the cost of going from a key to a key
def get_key_to_key(G, keys, doors, start_points, start_points_nums):
    key_to_key = collections.defaultdict(dict)

    key_to_bits = {k : 1 << k for k in keys.keys()}

    for start_point, start_point_num in zip(start_points, start_points_nums):
        start_point_bits = 1 << start_point_num
        for k, p in keys.items():
            k_bits = key_to_bits[k]
            res = get_distance(G, start_point, p, doors)
            if res is not None:
                distance, doors_in_way = res
                key_to_key[start_point_bits][k_bits] = (distance, doors_in_way)
    
    # this is all combination of two keys
    for k0, k1 in it.combinations(keys.keys(), 2):
        k0_bits = key_to_bits[k0]
        k1_bits = key_to_bits[k1]

        res = get_distance(G, keys[k0], keys[k1], doors)
        if res is not None:
            distance, doors_in_way = res
            key_to_key[k0_bits][k1_bits] = (distance, doors_in_way)
            key_to_key[k1_bits][k0_bits] = (distance, doors_in_way)

    return dict(key_to_key)

def find_next_possible_paths(key_to_key, path):
    current_positions = path.current
    for k0, v0 in key_to_key.items():
        if k0 & current_positions:
            for k1, v1 in v0.items():
                if not (k1 & path.collected_keys):
                    dist, doors_in_way = v1
                    if doors_in_way & path.collected_keys == doors_in_way:
                        new_position = current_positions ^ k0 | k1
                        yield Path(new_position, path.collected_keys + k1, path.length + dist)


def find_smallest_path(grid, keys, doors, start_points, max_x, max_y):
    G = build_graph(grid, max_x, max_y)

    total_keys = len(keys)
    
    # We set the start point bits to 1 since we are starting at them
    start_points_nums = list(range(len(start_points)))
    start_points_bits =  0 
    for x in start_points_nums:
        start_points_bits |= 1 << x

    key_to_key = get_key_to_key(G, keys, doors, start_points, start_points_nums)

    full_paths = []
    start_path = Path(start_points_bits, 0, 0)

    min_full_path_length = 10000000000000000000
    min_path_lengths = collections.defaultdict(int)

    counter = 0
    possible_paths = collections.deque([start_path])

    while possible_paths:
        counter += 1

        path = possible_paths.popleft()


        if min_path_lengths[path.get_state()] < path.length:
            continue

        possible_moves = []
        for new_path in find_next_possible_paths(key_to_key, path):
            if new_path.length < min_full_path_length:
                unique_state = new_path.get_state()
                better_path = False
                if unique_state in min_path_lengths:
                    if new_path.length < min_path_lengths[unique_state]:
                        min_path_lengths[unique_state] = new_path.length
                        better_path = True
                else:
                    min_path_lengths[unique_state] = new_path.length
                    better_path = True

                if better_path:
                    if new_path.path_length() == total_keys:
                        if new_path.length < min_full_path_length:
                            min_full_path_length = new_path.length

                        full_paths.append(new_path)
                    else:
                        possible_paths.append(new_path)

    return min([p.length for p in full_paths]), counter

    
grid, keys, doors, start_points, max_x, max_y = get_grid(part_b=True)
min_length, counter = find_smallest_path(grid, keys, doors, start_points, max_x, max_y)
print(min_length)


# This is "recoded", written without pasting, from the link below. I did this
# to learn how others have done this.
# https://topaz.github.io/paste/#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
