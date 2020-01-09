import math
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 0, -0.001)
y = (-3 * x * np.log(x) + np.exp(-(40 * (x - 1 / np.e)) ** 4) / 25) / 2
fig = plt.figure(figsize=(5,7))
plt.plot(y,x,"r-")
plt.show()
