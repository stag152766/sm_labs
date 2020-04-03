import numpy as np

stock = 100
value = 100

cash = 0
t = 1
T = np.zeros((361, 2), int)
T[0, 1] = 100
p = 0
probability = [0]

for i in range(100):
    while t <= 360:
        buy = 0
        sell = 0
        probability_yesterday = probability[t - 1]
        r = np.random.random()
        r = r * 100
        r = int(r)

        if r in range(0, 25):
            if probability_yesterday == 0:
                p = 1
            elif probability_yesterday == 1:
                p = -1
            else:
                p = 0

        elif int(r) in range(25, 50):
            if probability_yesterday == -1:
                p = 1
            elif probability_yesterday == 0:
                p = -1
            else:
                p = 0

        else:
            p = probability_yesterday

        probability.append(p)
        T[t, 1] = T[t - 1, 1] + p

        if T[t, 1] > T[t - 1, 1]:
            buy = 1
        elif T[t, 1] < T[t - 1, 1]:
            sell = 1

        if buy == 1 and cash > 0:
            new_stock = int(cash / T[t, 1])
            stock += new_stock
            cash -= new_stock * T[t, 1]
            new_stock = 0
        if sell == 1 and stock > 0:
            cash = stock * T[t, 1]
            stock = 0
        t += 1
    print(T[-1][-1])
    t = 0
