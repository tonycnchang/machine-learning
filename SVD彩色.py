from PIL import Image
import math
import matplotlib.pyplot as plt
import numpy as np

def restore(sigma,u,v,k):
    #print(k)
    m = len(u)
    n = len(v[0])
    a = np.zeros((m,n))
    for k in range(k+1):
        for i in range(m):
            a[i] += sigma[k] * u[i][k] * v[k]
    b = np.uint8(a)
    return b
    #Image.fromarray(b).save("svd_" + str(k) + ".png")
im = Image.open("bullet.jpg")#.convert("L")
data = np.asarray(im)
data0 = data[:,:,0]
data1 = data[:,:,1]
data2 = data[:,:,2]
u0,sig0,v0 = np.linalg.svd(data0)
u1,sig1,v1 = np.linalg.svd(data1)
u2,sig2,v2 = np.linalg.svd(data2)
x0 = restore(sig0,u0,v0,20)
x1 = restore(sig1,u1,v1,20)
x2 = restore(sig2,u2,v2,20)
pic = np.zeros(data.shape)
pic[:,:,0] = x0
pic[:,:,1] = x1
pic[:,:,2] = x2

imm = Image.fromarray(np.uint8(pic))#.save("fffff" + ".png")
imm.show()
"""
if __name__ == "__main__":
    u = np.random.uniform(0.0,1.0,10)
    print(u)
    plt.hist(u,80,facecolor="g",alpha=0.75)
    plt.grid(True)
    plt.show()
    times = 2
    for time in range(times):
        u += np.random.uniform(0.0,1.0,10)
    print(len(u))
    #u /= times
    print(len(u))
    plt.hist(u,80,facecolor="g",alpha=0.75)
    plt.grid(True)
    plt.show()
"""
