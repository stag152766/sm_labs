import numpy as np

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

x = int(input("Размер партии (Х): "))
h = int(input("Точка заказа (Н): "))

profit = 15
shipping_time = 5
cost_delivery = 500
cost_storage = 0.06

s = np.random.randint(0, x)

while t < 360:
    if s < h and f == 0:
        tau = np.random.randint(3, 7)
        tp = t + tau
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
print("Годовая прибыль:", y1)
