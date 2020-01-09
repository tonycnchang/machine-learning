import math
import numpy as np
import matplotlib.pyplot as plt

t = 10000
a = np.zeros(1000)
for i in range(t):
    a += np.random.uniform(-5, 5, 1000)
a /= t
plt.hist(a, bins=30, color='g', alpha=0.5, normed=True)
plt.grid()
plt.show()
