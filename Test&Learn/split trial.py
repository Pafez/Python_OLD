x,y,z = input("Expression → ").split()
a = int(x)
b = int(z)
if y == "+":
    print(a+b)
elif y == "-":
    print(a-b)
elif y == "*":
    print(a*b)
elif y == "/":
    print(a/b)