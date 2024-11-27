from os import system
system("clear")

while True:
    print("code:")
    try:
        inp = input()
        print("\noutput:")
        exec(inp)
        print("\n\n")
        input()
    except Exception as e:
        print("Error:",e,"\n\n")
        input()
    system("clear")
