import random
import math
import numpy as np

def is_same(a,b):
    n = len(a)
    for i in range(n):
        if math.fabs(a[i]-b[i]) > 1e-6:
            return False
    return True
if __name__ == "__main__":
    a = np.array([0.65,0.28,0.07,0.15,0.67,0.18,0.12,0.36,0.52])
    
    n = int(math.sqrt(len(a)))

    a = a.reshape((n,n))
    value,v = np.linalg.eig(a)

    times = 0
    while times==0 or not is_same(np.diag(a),v):
        v =np.diag(a)
        q,r = np.linalg.qr(a)
        a = np.dot(r,q)
        times += 1
        print("正交阵：",q)
        print("三角阵：",r)
        print("近似阵：",a)
    print("次数：",times,"近似值：",n.diag(a))
    print("精确特征值：",value)
