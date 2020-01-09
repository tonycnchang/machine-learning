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

    Image.fromarray(b).save("svd_" + str(k) + ".png")

im = Image.open("bullet.jpg").convert("L")
data = np.asarray(im)

u,sig,v = np.linalg.svd(data)

restore(sig,u,v,195)

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
