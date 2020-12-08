import fileinput as fi

print(sum(len(set.intersection(*map(set, x.split("\n")))) for x in "".join(fi.input()).split("\n\n")))
