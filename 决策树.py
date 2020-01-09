# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 11:56:33 2018

@author: lenovo
"""

import numpy as np

baseball = np.array([[0,0,1,2,2,2,1,0,0,2,0,1,1,2],#outlook
                     [0,0,0,0,1,1,1,0,1,1,1,0,1,0],#hunidity
                     [0,1,0,0,0,1,1,0,0,0,1,1,0,1]])#windy

target = np.array([[0,0,1,1,1,0,1,0,1,1,1,1,1,0]])#play
h_d0 = np.count_nonzero(target[0] == 0) / len(target[0])#不出去玩的天数所占比例
h_d1 = np.count_nonzero(target[0] == 1) / len(target[0])#出去玩的天数所占比例



a00,a01,a10,a11,a20,a21 = 0,0,0,0,0,0

h_d = 0
h_d_a_k = 0
h_d_a_i = 0
"""
#3个特征
h_a00 = np.count_nonzero(baseball[2] == 0)# / len(baseball[0])
h_a01 = np.count_nonzero(baseball[2] == 1)# / len(baseball[0])
h_a02 = np.count_nonzero(baseball[0] == 2)# / len(baseball[0])
h_a = [h_a00,h_a01,h_a02]
for t in range(len(target[0])):
    if target[0][t] == 0 :
        h_d += h_d0*np.log(h_d0)
        if baseball[0][t]  == 0:
            a00 += 1
        elif baseball[0][t]  == 1:
            a10 += 1
        else:
            a20 += 1
    else:
        h_d += h_d1*np.log(h_d1)
        if baseball[0][t]  == 0:
            a01 += 1
        elif baseball[0][t]  == 1:
            a11 += 1
        else:
            a21 += 1
            
data = [[a00,a01],[a10,a11],[a20,a21]]
"""
#2个特征
h_a00 = np.count_nonzero(baseball[2] == 0)# / len(baseball[0])
h_a01 = np.count_nonzero(baseball[2] == 1)# / len(baseball[0])
h_a = [h_a00,h_a01]
a00,a01,a10,a11 = 0,0,0,0
for t in range(len(target[0])):
    if target[0][t] == 0 :
        h_d += h_d0*np.log(h_d0)
        if baseball[0][t]  == 0:
            a00 += 1

        else:
            a10 += 1
    else:
        h_d += h_d1*np.log(h_d1)
        if baseball[0][t]  == 0:
            a01 += 1

        else:
            a11 += 1
data = [[a00,a01],[a10,a11]]

for i in range(len(data)):
    h_d_a_i += (h_a[i]/len(target[0]))*h_d_a_k
    h_d_a_k = 0
    for j in data[i]:
        if j != 0:
            h_d_a_k += (j/h_a[i])*np.log(j/h_a[i])

print(data)
print(h_a)
print(-h_d,-h_d_a_i)        
h_d_a = (-1*h_d) - (-1*h_d_a_i)
print(h_d_a)