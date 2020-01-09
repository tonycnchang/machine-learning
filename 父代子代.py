import random
import math
import numpy as np
A = np.around([[0.65,0.28,0.07],
              [0.15,0.67,0.18],
              [0.12,0.36,0.52]],decimals=3)
x = np.around([0.21,0.68,0.1],decimals=3)
y = np.around([0.75,0.15,0.1],decimals=3)
for i in range(10):
    x = np.around(np.dot(x,A),decimals=3)
    y = np.around(np.dot(y,A),decimals=3)
    print(x,y,sep="\n============================\n")
