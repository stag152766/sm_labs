import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3]
y = [1,2,3]
c = np.zeros((2, 2), int)
c[0, 0] = 1
c[0, 1] = 2
c[2, 0] = 4
c[2, 1] = 5
plt.axis[-2,2,-2,2]
plt.plot(c[0], c[1])
plt.show()


