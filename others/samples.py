import numpy as np

table = []
row = []


def rand(time):
    average = 0
    n = 100

    for i in range(n):
        r = np.random.random()
        t = -time * np.log(r)
        average += (t / n)
    return round(average, 2)


def fill_row():
    row.clear()
    for i in range(5):
        r = rand(5)
        row.append(r)
    table.append(row)


fill_row()
print(table)

fill_row()
print(table)