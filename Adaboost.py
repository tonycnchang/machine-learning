import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.array([0,1,2,3,4,5,6,7,8,9])
l = np.linspace(-2,2,10)
y = np.array([1,1,1,-1,-1,-1,1,1,1,-1])
g1 = np.array([0,0,0,0,0,0,0,0,0,0])
g2 = np.array([0,0,0,0,0,0,0,0,0,0])
g3 = np.array([0,0,0,0,0,0,0,0,0,0])
w1 = 0.1
fx = np.array([0,0,0,0,0,0,0,0,0,0])
for i in x:
    if i < 2.5:
        g1[i] = 1
    else:
        g1[i] = -1

e1 = np.count_nonzero(y != g1) / len(x)
alpha1 = 0.5 * np.log((1 - e1) / e1)
fx1 = alpha1 * g1
d2 = w1 * np.exp(-1*alpha1*y*g1)

for i in x:
    if i < 8.5:
        g2[i] = 1
    else:
        g2[i] = -1

for i in x:
    if i < 5.5:
        g3[i] = 1
    else:
        g3[i] = -1    
for i in x:    
    fx[i] = 0.4236*g1[i] + 0.6496*g2[i] + 0.7514*g3[i]

cm_light = mpl.colors.ListedColormap(['#A0FFA0', '#FFA0A0'])#,'#A0A0FF'
cm_dark = mpl.colors.ListedColormap(['g', 'r', 'b'])
x1, x2 = np.meshgrid(x, l)
y1 = np.tile(y,10).reshape(x1.shape)

plt.pcolormesh(x1, x2, y1, cmap=cm_light)
plt.scatter(x,y,c=fx,cmap=cm_dark)
plt.show()
