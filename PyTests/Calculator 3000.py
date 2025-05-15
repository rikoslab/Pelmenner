print("Welcome to the Calculator 3000")
print("Написано Низамиевым Тамирланом гр.533")

while True:
    res1 = False ## ФИКС.проверка сделан ли первый результат после деления
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
            print(int(result)) ## результат после деления
            res1 = True ## если произошло деление, повторонрого результата не будет выведено
        else:
            print("ERROR") ## команда на проверку деления на 0
            continue
    elif "*" in sign:
        result = a * b

    if res1 == False:
        print(int(result))
    else:
        print("")

    print("to Exit write 'exit' or press enter to continue ")
    exit = input()
    if exit == "exit":
        break
