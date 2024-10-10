X = [[3, 5, 35, 6, 4], [3, 96, 33, 4,] , [5, 3, 63, 1, 5]]


max_str = len(X[0])

X_temp = []
for l in X:
    X_temp.extend(l)
max_len = len(str(max(X_temp)))
print(max_len)


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
    on_list(list="")
    print("need help?")
    help_opt = input("Y|N\n")
    if help_opt == "Y" or help_opt == "y":
        print("1)Каждая строка и столбец высчитываются с нуля")
        print("2)Компоненты, строки и столбцы имеют только числовое значение")
        print("3)Если хотите сломать код - огорчу, он сломан")
    else:
        print("")
    row = int(input("row of list: "))
    column = int(input("col of list: "))
    index = int(input("index to change: "))
    X[row][column] = index
    print(X[row][column])


# ------------
# |3| 5|  3|6|
# ------------
# |3|96|  6|4|
# ------------
# |5| 3|643|1|
# ------------
