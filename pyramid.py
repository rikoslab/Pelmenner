while True:
    height = int(input(""))
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
    print("_" * 100)
    
    
