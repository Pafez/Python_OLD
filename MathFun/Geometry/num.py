err = 0

def area(a,b,c,d,e):
    if type(a) is str and type(b) is int and type(d) is int:
        if a == "parallelogram" or a == "rectangle" or a == "square" or a == "rhombos":
            A = b*d
        elif a == "triangle":
            A = (1/2)*b*d
        elif a == "circle":
            A = 3.14159265*b*d
        else:
            err = 2
            
        return print("The area of your",a,"is",A,"square metres.")
        
    elif type(a) is not str:
        err = 3
    elif type(b) is not int or type(d) is not int:
        err = 4
        
        
        
        
a = input("What is your polygon called? ")
b,c = input("First raw dimension = ").split()
d,e = input("Second raw dimension = ").split()

b = int(b)
d = int(d)

if c == "mm":
    b = b/1000
elif c == "cm":
    b = b/100
elif c == "km":
    b = b*1000
elif c == "m":
    "nothing"
else:
    err = 1

if e == "mm":
    d = d/1000
elif e == "cm":
    d = d/100
elif e == "km":
    d = d*1000
elif e == "m":
    "nothing"
else:
    err = 1

if err == 0:
    area(a,b,c,d,e)
elif err == 1:
    print("Scales are not valid")
elif err == 2:
    print("That polygon is not valid or supported yet")
elif err == 3:
    print("Polygon name must be in letters")
elif err == 4:
    print("Dimensions should only contain numbers with scales in letters")
    
    
