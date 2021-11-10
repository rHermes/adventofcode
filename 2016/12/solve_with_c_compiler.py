import fileinput as fi
import subprocess
import os

def gen_program(lines, part=1):
    prog = """
#include <stdio.h>
#include <inttypes.h>

int main() {
    intmax_t a, b, c, d;
    a = b = c = d = 0;
"""
    if part == 2:
        prog += "\tc = 1;\n"

    for i, line in enumerate(lines):
        prog += "L{}:".format(i)
        
        opt, *args = line.split()

        if opt == "inc":
            prog += "\t{}++;\n".format(args[0])
        elif opt == "dec":
            prog += "\t{}--;\n".format(args[0])
        elif opt == "cpy":
            prog += "\t{} = {};\n".format(args[1], args[0])
        elif opt == "jnz":
            prog += "\tif ({} != 0) goto L{};\n".format(args[0], i + int(args[1]))

    prog += "L{}:".format(i+1)
    prog += """\tprintf("%"PRIdMAX"\\n", a);\n"""
    prog += "\treturn 0;\n}\n"

    return prog


def solve(lines, part=1, clang=True):
    prog = gen_program(lines, part=part)
    fn = ".part{}".format(part)
    
    if clang:
        gens = subprocess.run(["clang", "-std=c99", "-O2", "-x", "c", "-", "-o", fn], input=prog.encode("latin1"))
    else:
        gens = subprocess.run(["gcc",  "-std=c99", "-O2", "-x", "c", "-", "-o", fn], input=prog.encode("latin1"))
    gens.check_returncode()

    calc = subprocess.run(["./{}".format(fn)], capture_output=True, text="latin1")
    os.remove(fn)
    calc.check_returncode()

    ans = int(calc.stdout)


    return ans
    

lines = [x for x in map(str.rstrip, fi.input()) if x]
print("Part 1:", solve(lines, part=1, clang=True))
print("Part 2:", solve(lines, part=2, clang=True))
