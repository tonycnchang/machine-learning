import numpy as np
import math
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.lines import Line2D
from matplotlib import cm

x = np.linspace(0,2*np.pi,20)
t = np.linspace(-1,1,20,endpoint=False)
y = np.abs(t)
#y = np.tile(y,5)

f = np.fft.fft(y)/20

f_real = np.real(f)
eps = 0.1*f_real.max()

f_real = np.where(np.fabs(f_real[:])<eps,0,f_real)

f_imag = np.imag(f)
eps = 0.1*f_imag.max()
f_imag = np.where(np.fabs(f_imag[:])<eps,0,f_imag)
f1 = f_real + f_imag * 1j
y1 = np.fft.ifft(f1)

fig = plt.subplot(221)
fig.plot(x,y,"r-")
fig = plt.subplot(222)
fig.stem(x,f,"r-","ro")
fig = plt.subplot(223)
fig.plot(x,y1,"r-")

plt.show()

"""
for i in range(2,15):
    x = np.linspace(0,i*2*np.pi,100)
    
    sinx = np.sin(x)

    sumx += sinx
  
fig1 = plt.figure()

plt.plot(np.linspace(0,2*np.pi,100),sumx,"r-")

#plt.plot(nn,ss,"bo")
#plt.plot(nn,cc,"go")

plt.show()
"""
