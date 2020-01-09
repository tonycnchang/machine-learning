import math
import numpy as np
import matplotlib.pyplot as plt

"""
t1 = np.arange(-np.pi,np.pi,0.02)
t2 = np.arange(0,8*np.pi,0.1)

a = 1
x = a*(1-np.cos(t1))
y = a*(1-np.sin(t1))
fig1 = plt.subplot(polar="True")
#fig2 = plt.subplot(122,projection="polar")
fig1.plot(x,y,"r-")
#fig2.plot(t2,b,"ro")
plt.show()
"""
#y = np.sin(t1)*(np.fabs(np.cos(t1))**0.5)/(np.sin(t1)+7/5) - 2*np.sin(t1) +2
t = np.linspace(0, 7, 100)
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

plt.plot(x,y,"r-")
plt.show()
