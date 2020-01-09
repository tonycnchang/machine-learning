import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

if __name__ == "__main__":
    fig = plt.figure()
    ax = fig.add_subplot(111)
    u = np.linspace(0,4,20)
    x,y = np.meshgrid(u,u)
    z = np.log(np.exp(x)+np.exp(y))
    #ax.contourf(x,y,z,20)
    ax = Axes3D(fig)
    ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.viridis)
    plt.show()

