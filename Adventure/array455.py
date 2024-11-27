#-*-coding:utf8;-*-
#qpy:console

import array as arr
c = int(input("Enter number → "))
d = int(input("Enter number → "))
e = int(input("Enter number → "))

b = int(input("Which number do you want? → "))

if b == 1:
    print(c)
elif b == 2:
    print(d)
elif b == 3:
    print(e)
else:
    print("Not in the list")