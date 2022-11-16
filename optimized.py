import time

start = time.time()
datas = []


def get_combination(max_value, elements):
    return 0, 0, []


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
