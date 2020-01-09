import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.1,10,0.1)
y = -x * np.log(x)
plt.plot(x,y,"r*")
plt.show()

