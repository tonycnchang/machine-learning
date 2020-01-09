import math
import numpy as np
import matplotlib.pyplot as plt

sigma1 = np.arange(0,8*np.pi,0.02)
sigma2 = np.arange(0,8*np.pi,0.1)
a = sigma1/6
b = sigma2/6
fig1 = plt.subplot(121,projection="polar")
fig2 = plt.subplot(122,projection="polar")
fig1.plot(sigma1,a,"r-")
fig2.plot(sigma2,b,"ro")
plt.show()
