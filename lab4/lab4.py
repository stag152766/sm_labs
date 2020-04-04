import random

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# сальдо на начало периода
balance = 0
t = 0
customers = np.zeros((720, 7), int)
id = 0
id_inn = 0
t_balance = np.zeros((120, 2), int)

while t < 120:
    new_customer = np.random.randint(2, 6)
    for i in range(new_customer):
        # стоимость квартиры
        osn = random.randrange(500000, 3000000, 100000)
        # период накопления
        accumulation_period = np.random.randint(1, 36)
        # cрок рассочки
        repayment_period = np.random.randint(36, 120)

        # ежемесячные платежи
        monthly_accumulation_payment = osn / (2 * accumulation_period)
        monthly_repayment_payment = osn / (2 * repayment_period)

        customers[id, 0] = id
        customers[id, 1] = osn
        customers[id, 2] = accumulation_period
        customers[id, 3] = repayment_period
        customers[id, 4] = monthly_accumulation_payment
        customers[id, 5] = monthly_repayment_payment
        customers[id, 6] = t
        id += 1

    for customer in customers:
        if customer[1] != 0:
            if t < customer[2]:
                balance += customer[4]
            elif t == customer[2]:
                balance += customer[4]
                balance -= customer[1]
            elif customer[2] < t <= customer[3]:
                balance += customer[5]

            # t_balance[id_inn, 0] = t
            # t_balance[id_inn, 1] = customer[0]
            # t_balance[id_inn, 2] = balance
            # id_inn += 1
            t_balance[t, 0] = t
            t_balance[t, 1] = balance

    t += 1

x = []
y = []
for i in range(len(t_balance)):
    x.append(t_balance[i, 0])
    y.append(t_balance[i, 1])

plt.axis([0, 120, -100000000, 100000000])

min_balance = min(y)
index = y.index(min_balance)
min_day = x[index]
print(min_balance)
print(min_day)

plt.plot(x, x)
plt.scatter(min_day,min_balance,color='orange', s=40, marker='o')
for i in t_balance:
    plt.plot(x, y, color='red')
plt.show()
