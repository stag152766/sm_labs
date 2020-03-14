import numpy as np

table = []
row = []

t_start = 0
array_1  = {}


def rand(time):
    average = 0
    n = 100

    for i in range(n):
        r = np.random.random()
        t = -time * np.log(r)
        average += (t / n)
    return average


for i in range(10):
    t_load = round(rand(5), 2)
    t_road = round(rand(60), 2)
    # номер самосвала
    row.append(i + 1)
    # начало загрузки
    row.append(round(t_start, 2))
    # конец загрузки
    row.append(round(t_start + t_load, 2))
    # время в пути
    row.append(t_road)
    # время возвращения
    row.append(round(t_start + t_load + t_road, 2))
    array_1[i + 1] = round(t_start + t_load + t_road, 2)
    # порядковый номер рейса
    row.append(i + 1)

    # начало следующей загрузки
    t_start += t_load + 0.01
    copy_row = row[:]
    table.append(copy_row)
    row.clear()

for i in range(10, 20):
    t_load = round(rand(5), 2)
    t_road = round(rand(60), 2)
    # поиск самосвала который вернулся раньше
    car_id = min(array_1, key=lambda k: array_1[k])
    # номер самосвала
    row.append(car_id)

    # формируется очередь под загрузку
    t_back = min(array_1.values())
    t_start = t_back + 0.01
    t_finish = table[-1][2]
    if t_start < t_finish:
        t_start = t_finish + 0.01

    # начало загрузки
    row.append(round(t_start, 2))
    # конец загрузки
    row.append(round(t_start + t_load, 2))
    # время в пути
    row.append(t_road)
    # время возвращения
    row.append(round(t_start + t_load + t_road, 2))
    array_1[i + 1] = round(t_start + t_load + t_road, 2)
    # порядковый номер рейса
    row.append(i + 1)
    copy_row = row[:]
    table.append(copy_row)
    row.clear()
    array_1[car_id] = 10000

print("%7s%12s%12s%12s%12s%12s" % ('#', 'start', 'finish', 'time', 'back', 'count'))
for i in range(len(table)):
    current_row = table[i]
    for j in current_row:
        print("%7s" % (j), end="\t\t")
    print('\r')