# Success #

import os

os.chdir("../Memorytest/")

l = os.listdir()

try:
    print(l[0],"should say 'Blocks'")
except:
    print("There is no data")