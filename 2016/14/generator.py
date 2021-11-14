import hashlib

salt = "zpqevtbw"
salt = "abc"
index = 0


with open("test.txt", "w") as f:
    while True:
        g = hashlib.md5("{}{}".format(salt, index).encode("latin1"))
        # print(g.hex())
        f.write("{} {}\n".format(index, g.hexdigest()))
        index += 1


