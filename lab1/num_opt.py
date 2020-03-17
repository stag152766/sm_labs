import numpy as np

y = 0
dy = 0
d = 0
sy = 0
q = 0
k = 200
x = 600
h = 300

profit = 15
shipping_time = 5
cost_delivery = 500
cost_storage = 0.06

for k in range(k):
    # прибыль
    y1 = 0
    # объем продаж
    y2 = 0
    # затраты на доставку
    y3 = 0
    # затраты на хранение
    y4 = 0
    # время поступления партии товара
    tp = 0
    # наличие заказа
    f = 0
    # текущий день
    t = 0

    s = np.random.randint(0, x)
    while t < 360:
        if s < h and f == 0:
            q = np.random.randint(3, 7)
            tp = t + q
            f = 1
            y3 = y3 + cost_delivery
        if t == tp:
            s = s + x
            f = 0
        u = np.random.randint(20, 60)
        if u > s:
            u = s
        s = s - u
        y2 = y2 + u
        y4 = y4 + s * cost_storage
        t += 1
    y1 = y2 * profit - y3 - y4
    sy = sy + y1
    dy = dy + y1 * y1

# выборочная дисперсия выходной переменной
dy = (k * dy - sy * sy) / (k * k)
# выборочное среднее квадратичное отклонение выходной переменной
q = np.sqrt(dy)
# точность определения среднего значения Y1 при уровне достоверности 0.95
d = 1.96 * (q / np.sqrt(k))
# выборочное среднее значение выходной переменной
sy = sy / k
k = (1.96 * 1.96 * q * q) / 1

print()