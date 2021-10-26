import fileinput as fi


# current straterg

points = []
for line in map(str.rstrip,fi.input()):
    x, y = map(int, line.split(", "))
    points.append((x,y))


minx, miny = min(points)
print(min(points))
print(max(points))
