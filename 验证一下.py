import numpy as np
import math
import matplotlib.pyplot as plt
import operator
from functools import reduce
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
"""
#np.stack合并两矩阵
#flat返回矩阵中的每个元素
a = np.arange(0, 60, 10).reshape((-1, 1)) + np.arange(6)
b = np.arange(100, 160, 10).reshape((-1, 1)) + np.arange(6)
c = np.stack((a.flat , b.flat),axis=1)
print(c)
#print (a[(0,1,2,3), (2,3,4,5)])

#a = reduce(operator.mul,(2,3,4))
#print(a)
"""

"""
#np.where()
t = np.linspace(-1, 1, 10, endpoint=False)

y = np.where(t < 0, -t, 0)

y = np.where(t >= 0, t, y)

plt.plot(t,y,"r-")
plt.show()
"""
"""
#meshgrid
#mpl.colors.ListedColormap
a = np.arange(0, 10, 0.1)
b = np.arange(0, 10, 0.1)
cm_light = mpl.colors.ListedColormap(['#A0FFA0', '#FFA0A0', '#A0A0FF'])
x,y = np.meshgrid(a,b)

z = x + y**2 +1

plt.pcolormesh(x, y, z, cmap=cm_light)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm_light)

plt.show()
"""

x = np.linspace(0,1,50)*2*np.pi

y1 = np.sin(x)
y2 = np.cos(x)
    
plt.plot(y1,y2,"r-")
plt.pause(0.2)

