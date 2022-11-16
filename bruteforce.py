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


with open("data/dataset_1.csv") as file:
    reader = file.readlines()[1:]
    for row in reader:
        temp = row.split(",")
        datas.append((temp[0], float(temp[1]), float(temp[1])*(1+float(temp[2])/100)-float(temp[1])))
profit, actions = get_combination(500, datas)
print("Actions: " + str([action[0] for action in actions]))
print('Total cost = {:.2f}€'.format(sum([action[1] for action in actions])))
print('Total profit = {:.2f}€'.format(profit))
print('Solution found in {:}ms'.format(round(1000*(time.time() - start))))
