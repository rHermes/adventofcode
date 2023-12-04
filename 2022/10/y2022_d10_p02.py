import fileinput as fi
import itertools as it

FILL_CHAR = "#"
# FILL_CHAR = "█"


def get_instructions():
    for line in filter(bool, map(str.rstrip, fi.input())):
        if line.startswith("addx "):
            yield "noop"

        yield line

def draw(cycle, reg, canvas):
    y, x = divmod(cycle - 1, 40)
    # y = (cycle-1) // 40
    # x = (cycle-1) % 40

    if reg - 1 <= x <= reg + 1:
        canvas[y][x] = FILL_CHAR

letters = [
(" ##  #  # #  # #### #  # #  # ", 'A'),
("###  #  # ###  #  # #  # ###  ", 'B'),
(" ##  #  # #    #    #  #  ##  ", 'C'),
("#### #    ###  #    #    #### ", 'E'),
("#### #    ###  #    #    #    ", 'F'),
(" ##  #  # #    # ## #  #  ### ", 'G'),
("#  # #  # #### #  # #  # #  # ", 'H'),
(" ###   #    #    #    #   ### ", 'I'),
("  ##    #    #    # #  #  ##  ", 'J'),
("#  # # #  ##   # #  # #  #  # ", 'K'),
("#    #    #    #    #    #### ", 'L'),
(" ##  #  # #  # #  # #  #  ##  ", 'O'),
("###  #  # #  # ###  #    #    ", 'P'),
("###  #  # #  # ###  # #  #  # ", 'R'),
(" ### #    #     ##     # ###  ", 'S'),
("#  # #  # #  # #  # #  #  ##  ", 'U'),
("#    #     # #   #    #    #  ", 'Y'),
("####    #   #   #   #    #### ", 'Z'),
]


def parse_display(display: list[list[str]]) -> str:
    pass



def solve():
    reg = 1
    canvas = [[' ' for _ in range(40)] for _ in range(6)]

    draw(1, reg, canvas)
    
    # We start at 2, as that is, as the cylce here, is the one more
    # than the current cycle we are on, and we would normally start on 1
    for cycle, inst in enumerate(get_instructions(), start=2):
        parts = inst.split(" ")
        if parts[0] == "addx":
            reg += int(parts[1])

        draw(cycle, reg, canvas)

    strs = ["".join(row) for row in canvas]
    return "\n".join(strs)

print(solve())
