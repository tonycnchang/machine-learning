import math
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    nn = []
    zz = []
    x = np.array([[5],[1]])
    y = np.array([[2],[3]])
for i in range(11):
    n = i/10
    z = n*x+(1-n)*y
    nn.append(z[0])
    zz.append(z[1])
    print(z)
plt.plot(nn,zz,"g-",linewidth=2)
plt.show()

"""    
    x = [float(i)/100 for i in range(1,300)]
    y = [math.log(i) for i in x]
    plt.plot(x,y,"r-",linewidth=3,label="logcurve")
    a = [x[20],x[175]]
    b = [y[20],y[175]]
    
    plt.plot(a,b,"g-",linewidth=2)
    plt.plot(a,b,"b*",markersize=15,alpha=0.75)
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.xlabel("x")
    plt.xlabel("log(x)")
    
    plt.show()
"""
