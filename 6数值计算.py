import numpy as np
import math
from functools import reduce
import operator

def jc(n,k):
    return reduce(operator.mul,range(n-k+1,n+1))/reduce(operator.mul,range(1,k+1))

def bagging(n,p):
    s = 0
    for i in range(int(n/2)+1,n+1):
        s += jc(n,i)*p**i*(1-p)**(n-i)
    return s

for t in range(9,100,10):
    print(t,"采样正确率：",bagging(t,0.6))
