import fileinput


def solve(s):
    dims = len(s)//(25*6)
    img = [["2" for _ in range(25)] for _ in range(6)]
    for i in range(dims):
        # Create subset view of img
        k = s[i*(25*6):(i+1)*(25*6)]
        # This will create 25 iterators and zip them. This causes it to group by
        # 25 increments
        grouper =[iter(k)]*25
        pv = zip(*grouper)
        for j, row in enumerate(pv):
            for i, px in enumerate(row):
                if img[j][i] == "2" and px != "2":
                    if px == "1":
                        img[j][i] = "@"
                    else:
                        img[j][i] = " "

    
    return "\n".join("".join(x) for x in img)


for line in fileinput.input():
    print(solve(line.strip()))
