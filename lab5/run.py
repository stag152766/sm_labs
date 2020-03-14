import numpy as np

table = []
row = []
array = {}
t_start = 0


def expo(time):
    average = 0
    n = 100
    for i in range(n):
        r = np.random.random()
        t = -time * np.log(r)
        average += (t / n)
    return round(average, 2)


def set_loop(first, last, t_start):
    for i in range(first, last):
        t_load = expo(5)
        t_road = expo(60)

        # номер самосвала
        if i < 10:
            row.append(i + 1)
        else:
            # поиск самосвала который вернулся раньше
            car_id = min(array, key=lambda k: array[k])
            # номер самосвала
            row.append(car_id - first + 10)

            # формируется очередь под загрузку
            t_back = min(array.values())
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
        array[i + 1] = round(t_start + t_load + t_road, 2)
        # порядковый номер рейса
        row.append(i + 1)

        # начало следующей загрузки
        if i < 10:
            t_start += t_load + 0.01
        else:
            array[car_id] = 10000

        copy_row = row[:]
        table.append(copy_row)
        row.clear()

        if t_start >=480:
            return


def print_table():
    global i
    print("%7s%16s%16s%16s%16s%16s" % ('car_id', 't_start', 't_finish', 't_road', 't_back', 'count'))
    for i in range(len(table)):
        current_row = table[i]
        for j in current_row:
            print("%7s" % (j), end="\t\t")
        print('\r')

for r in range(10, 90, 10):
    first = r - 10
    last = r
    set_loop(first, last, t_start)
print_table()