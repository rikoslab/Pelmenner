# while True:
#     height = int(input(""))
if True:
    height = 5
    sp = height
    y = 1
    while y <= height:
        while sp > 0:
            x = 1
            print(" " * sp, end="")
            while x < y:
                print("*", end="")
                x += 1
            z = 0
            while z < y:
                print("*", end="")
                z += 1
            y += 1
            sp -= 1
            print("")
    while y >= 0:   
        y -= 1
        while sp <= height:
            print(" " * sp, end="")
            sp += 1
        print("$")
    print("__" * height)
    
    
