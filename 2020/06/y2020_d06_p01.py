import fileinput

print(sum(len(set(x) - set("\n")) for x in "".join(fileinput.input()).split("\n\n")))
