import numpy as np
import matplotlib.pyplot as plt
a = np.arange(-1.5,1.52,0.02)
b = np.fabs(a)
y = b**b
fig = plt.figure()
plt.plot(a,y,"r-")
plt.show()
