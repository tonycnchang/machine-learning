import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,10000)
y = np.random.randn(10000)

plt.plot(x,y,"ro")
plt.show()
