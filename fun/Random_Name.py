import random

list1 = []
list2 = []

while True:
    input()
    name1 = list1[random.randint(0,len(list1)-1)]
    name2 = list2[random.randint(0,len(list2)-1)]
    
    name = name1 + " " + name2
    print(name)
