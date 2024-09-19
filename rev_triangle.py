while True:

    height = int(input(""))
    y = height
    while y > 0:
        x = 0
        while x < y:
            print("*", end="")
            x += 1
        y -= 1
        print("")
    
