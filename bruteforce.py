import time
import sys

sys.setrecursionlimit(2000)
start = time.time()
datas = []


def get_combination(max_value, elements, elements_selection=None):
    if elements_selection is None:
        elements_selection = []
    if elements:
        val1, cost, lst_val1 = get_combination(max_value, elements[1:], elements_selection)
        val = elements[0]
        if val[1] <= max_value:
            val2, cost, lst_val2 = get_combination(max_value - val[1], elements[1:], elements_selection + [val])
            if val1 < val2:
                return val2, cost, lst_val2
        return val1, cost, lst_val1
    else:
        cost = sum([i[1] for i in elements_selection])
        return sum([i[2] for i in elements_selection]) - cost, cost, elements_selection


with open("data/dataset_1.csv") as file:
    reader = file.readlines()[1:]
    for row in reader:
        temp = row.split(",")
        datas.append((temp[0], float(temp[1]), float(temp[1])*(1+float(temp[2])/100)))
profit, total_cost, actions = get_combination(500, datas)
print("Actions: " + str([action[0] for action in actions]))
print('Total cost = {:.2f}€'.format(total_cost))
print('Total profit = {:.2f}€'.format(profit))
print('Solution found in {:}ms'.format(round(1000*(time.time() - start))))
