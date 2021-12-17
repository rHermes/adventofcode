import fileinput as fi

ymin = int(next(fi.input()).rstrip().split()[3][2:].split("..")[0])
assert(ymin <= 0)

# Since it's a parobola, the ball is going to come down to y=0 again, with
# the velocity -(dy+1), where dy is the initial velocity. This means that
# we just have to find the biggest dy that doesn't immidiatily go below the
# target area. This is always going to be dy = (-ymin)-1.
#
# The height of the arch is the sum of the triangle numbers, so we get
# (dy*(dy+1))//2, which when we insert dy = (-ymin)-1 we get
# (ymin*(ymin+1))//2, which is the answer.
print((ymin*(ymin+1))//2)
