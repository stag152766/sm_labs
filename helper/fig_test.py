import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3]
y = [[1,2,3],[4,5,6],[7,8,9]]
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("A test graph")
for i in range(len(y[0])):
    plt.plot(x,[pt[i] for pt in y],label = 'id %s'%i)
plt.legend()
plt.show()


