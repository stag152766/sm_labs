import numpy as np

y=0
yopt = 0
xopt = 0

hopt = 0

profit = 15
shipping_time = 5
cost_delivery = 500
cost_storage = 0.06

for x in range(400, 1000, 100):
    for h in range(120, 360, 30):
        for k in range(400):
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
                y1 = y1 + y2 * profit - y3 - y4
                t += 1
            y = y1
            if y > yopt:
                yopt = y
                xopt = x
                hopt = h

print("Годовая прибыль:", yopt)
print("Размер партии:", xopt)
print("Точка заказа:", hopt)
