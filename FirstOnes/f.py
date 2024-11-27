x = int(input("Type the first number → "))
y = int(input("Type the second number → "))
z = input("Type the operation you want to do between them → ")
if z == "add":
    print ("Answer = ",x+y)
elif z == "substract":
    print ("Answer = ",x-y)
elif z == "multiply":
    print ("Answer = ",x*y)
elif z == "divide":
    print ("Answer = ",x/y)
elif z == "exponentiate":
    print ("Answer = ",x**y)
elif z == "remainder":
    print ("Answer = ",x%y)
else:
    print ("Invalid Operation Type")

print("Thanks For Using Me! ---Calculator")