import fileinput

print(sum(l[(i*3) % (len(l)-1)] == '#' for (i,l) in enumerate(fileinput.input())))
