import time

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


with open("data/dataset_2.csv") as file:
    reader = file.readlines()[1:]
    for row in reader:
        temp = row.split(",")
        cost = round(float(temp[1])*100)
        if cost > 0:
            profit = cost*float(temp[2])/100
            datas.append((temp[0], cost, profit))
profit, actions = get_combination(50000, datas)
print("Actions: " + str([action[0] for action in actions]))
print('Total cost = {:.2f}€'.format(sum([action[1]/100 for action in actions])))
print('Total profit = {:.2f}€'.format(profit/100))
print('Solution found in {:}ms'.format(round(1000*(time.time() - start))))
