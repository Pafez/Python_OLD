def anim1(n):
    c1 = "-"
    c2 = "\\"
    c3 = "|"
    c4 = "/"
    if n == 1:
        return c1
    elif n == 2:
        return c2
    elif n == 3:
        return c3
    elif n == 4:
        return c4

def anim2(n):
    c1 = "."
    c2 = ".."
    c3 = "..."
    if n == 1:
        return c1
    elif n == 2:
        return c2
    elif n == 3:
        return c3
