x = 0
y = 0
z = 0

while -1000 <= x <= 1000 and -1000 <= y <= 1000 and -1000 <= z <= 1000:
    print (x, y, z)
    f = int(input("Forward"))
    b = int(input("Backward"))
    u = int(input("Upward"))
    d = int(input("Downward"))
    r = int(input("Right"))
    l = int(input("Left"))
    x = x + f - b
    y = y + u - d
    z = z + r - l
else:
    print ("Out of the region")
