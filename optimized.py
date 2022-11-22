import time
import sys

start = time.time()
datas = []


def get_combination(max_value, elements):
    matrice = [[0 for x in range(max_value + 1)] for x in range(len(elements) + 1)]
    for i in range(1, len(elements) + 1):
        for w in range(1, max_value + 1):
            if elements[i-1][1] <= w:
                matrice[i][w] = max(elements[i-1][2] + matrice[i-1][w-elements[i-1][1]], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]

    w = max_value
    n = len(elements)
    elements_selection = []
    while w >= 0 and n >= 0:
        e = elements[n-1]
        if matrice[n][w] == matrice[n-1][w-e[1]] + e[2]:
            elements_selection.append(e)
            w -= e[1]
        n -= 1
    return matrice[-1][-1], elements_selection


def read_datas():
    with open(sys.argv[1]) as file:
        reader = file.readlines()[1:]
        for row in reader:
            split_row = row.split(",")
            datas.append((split_row[0], float(split_row[1]), float(split_row[1]) * float(split_row[2]) / 100))


def show_results():
    profit, actions = get_combination(500, datas)
    print("Actions: " + str([action[0] for action in actions]))
    print('Total cost = {:.2f}€'.format(sum([action[1] for action in actions])))
    print('Total profit = {:.2f}€'.format(profit))
    print('Solution found in {:}ms'.format(round(1000 * (time.time() - start))))


if len(sys.argv) > 1:
    temp = sys.argv[1].split(".")
    if len(temp) > 1 and temp[1] == "csv":
        try:
            read_datas()
            show_results()
        except FileNotFoundError:
            print("The file doesn't exists")
    else:
        print("The file must be a .csv")
else:
    print("You need to specify the path to the data file")
