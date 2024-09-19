while True:

    height = int(input(""))
    y = 1
    while y <= height:
        x = 0
        while x < y:
            print("*", end="")
            x += 1
        y += 1
        print("")
    
