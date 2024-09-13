print("Welcome to the Calculator 3000")
print("Написано Низамиевым Тамирланом гр.533")

while True:

    a = float(input('write first number: '))
    b = float(input('write second number: '))
    sign = input('write a sign(+, -, /, *): ')

    if "+" in sign:
        result = a + b
    elif "-" in sign:
        result = a - b
    elif "/" in sign:
        if b != 0:
            result = a / b
            print(int(result))
        else:
            print("ERROR")
            continue
    elif "*" in sign:
        result = a * b

    print(int(result))

    print("to Exit write 'exit' or press enter to continue ")
    exit = input()
    if exit == "exit":
        break
