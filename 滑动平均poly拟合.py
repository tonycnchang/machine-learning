import numpy as np
import matplotlib.pyplot as plt
n = 10
x = np.arange(0,10,0.1)
t = np.arange(0.1*(n-1),10,0.1)

c = np.random.uniform(-1,1,100)
w = np.ones(n)
w /= w.sum()
print(w)
y = 3*np.sin(x)+5
yc = y + 0.2*c
z = np.convolve(yc,w,"valid")

#poly = np.polyfit(x,yc,6)
#z_poly = np.polyval(poly,x)

poly = np.polyfit(t,z,6)
z_poly = np.polyval(poly,t)

plt.plot(x,yc,"g.")
plt.plot(x,y,"y-")
plt.plot(t,z,"r-")
#plt.plot(x,z_poly,"b-")
plt.plot(t,z_poly,"b-")
plt.show()

