import math
import numpy as np
import matplotlib.pyplot as plt
a = np.arange(-3,3.1,0.1)
sigma = 1
mu = 0
y = 1/(math.sqrt(2*math.pi)*sigma)*math.e**(-(a-mu)**2/2*sigma**2)
fig = plt.figure()
plt.plot(a,y,"r-")
plt.plot(a,y,"go")
plt.show()
