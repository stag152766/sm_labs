import random

import numpy as np

amount = 0
income = 0
t = 0
customers = [[], [], [], [], [], [], []]
index = 0

while t < 120:
    new_customer = np.random.randint(2, 6)
    for i in range(new_customer):
        osn = random.randrange(500000, 3000000, 100000)
        accumulation_period = np.random.randint(1, 36)
        repayment_period = np.random.randint(36, 120)

        monthly_accumulation_payment = osn / accumulation_period
        monthly_repayment_payment = osn / repayment_period

        customers[0].append(index)
        customers[1].append(osn)
        customers[2].append(accumulation_period)
        customers[3].append(repayment_period)
        customers[4].append(monthly_accumulation_payment)
        customers[5].append(monthly_repayment_payment)
        customers[6].append(t)
        index +=1

    for all in customers[2]:
        if t < a
    if t <
    t += 1

print()
