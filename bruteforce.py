import time
import sys

sys.setrecursionlimit(2000)
start = time.time()
datas = []


def get_combination(max_value, elements, elements_selection=None):
    if elements_selection is None:
        elements_selection = []
    if elements:
        val1, lst_val1 = get_combination(max_value, elements[1:], elements_selection)
        val = elements[0]
        if val[1] <= max_value:
            val2, lst_val2 = get_combination(max_value - val[1], elements[1:], elements_selection + [val])
            if val1 < val2:
                return val2, lst_val2
        return val1, lst_val1
    else:
        return sum([i[2] for i in elements_selection]), elements_selection


def read_datas():
    with open(sys.argv[1]) as file:
        reader = file.readlines()[1:]
        for row in reader:
            split_row = row.split(",")
            datas.append((split_row[0], float(split_row[1]), float(split_row[1]) * float(split_row[2]) / 100))


def show_results():
    profit, actions = get_combination(500, datas)
    print("Actions list:")
    for action in actions:
        print(action[0] + "\t | cost: " + str(action[1]) + "€\t | profit: " + str(action[2]) + "€")
    print('\nTotal cost = {:.2f}€'.format(sum([action[1] for action in actions])))
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
