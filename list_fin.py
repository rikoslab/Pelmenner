X = [[3, 5, 35, 6, 4], [3, 96, 33, 4, 5] , [5, 3, 63, 1, 5]]





def on_list(list):
    n = 0
    print("-" * (((max_str) * (max_len + 1)) + 1))
    for x in X:
        list = (" " * (max_len - len(str(i))) + str(i) for i in X[n])
        print("|", end="")
        print("|".join(list), end="|\n")
        n +=1
        print("-" * (((max_str) * (max_len + 1)) + 1))


# "-" * (кол-во ячеек * (max_len + 1) + 1)
while True:
    max_str = len(X[0])

    X_temp = []
    for l in X:
        X_temp.extend(l)
    max_len = len(str(max(X_temp)))
    print(max_len)

    on_list(list="")
    print("Need help?")
    help_opt = input("Y|N\n")
    if help_opt == "Y" or help_opt == "y":
        print("1)Каждая строка и столбец высчитываются с нуля")
        print("2)Компоненты, строки и столбцы имеют только числовое значение")
        print("3)Если хотите сломать код - огорчу, он сломан")
    elif help_opt == "N" or help_opt == "n":
        print("")
    elif help_opt == "quit":
        break
    else:
        print("ну ладно")
        
    row = input("row of list: ")

    while not row.isdigit():
        print("ЗНАЧЕНИЕ СТРОКИ ЭТО НЕ БУКВЫ И НЕ ПУСТОТА")
        row = input("row of list: ")
    row = int(row)
    while row > 2:
        print("Значения '", row ,"' нет в данном листе")
        row = int(input("row of list: "))

    column = input("col of list: ")

    while not column.isdigit():
        print("ЗНАЧЕНИЕ СТОЛБЦОВ ЭТО НЕ БУКВЫ И НЕ ПУСТОТА")
        column = input("col of list: ")
    column = int(column)
    while column > 4:
        print("Значения '", column ,"' нет в данном листе")
        column = int(input("col of list: "))
    
    index = input("index to change: ")

    while not index.isdigit():
        print("ЗНАЧЕНИЕ СТОЛБЦОВ ЭТО НЕ БУКВЫ И НЕ ПУСТОТА")
        index = input("index to change: ")
    index = int(index)
    X[row][column] = index
    print(X[row][column])



# ------------
# |3| 5|  3|6|
# ------------
# |3|96|  6|4|
# ------------
# |5| 3|643|1|
# ------------
