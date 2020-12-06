import fileinput as fi
from functools import reduce
from operator import and_ 

print(sum(len(reduce(and_, map(set, x.split("\n")))) for x in "".join(fi.input()).split("\n\n")))
