import numpy as np
import matplotlib.pyplot as plt
#np.random.seed(0)

#x1 = np.linspace(-2,-0.5,10)
#x2 = np.linspace(0.5,2,10)
#z1,z2 = np.ones(len(x1))*-1,np.ones(len(x2))
#z = np.hstack((z1,z2))
#x = np.hstack((x1,x2))
#y = x + np.random.randn(len(x))
#data = np.stack((x,y,z),axis=1).T

h_a,target = 0,0
data = np.array([[3,3,1],
                 [4,3,1],
                 [1,1,-1]])
a = 1/len(data[2])*data[2]
for i in range(len(data[0])):
    h_a += a[i]
    for j in range(len(data[1])):
        if i == j:
            
        target += 1/2*a[i]*a[j]*data[2][i]*data[2][j]*(np.dot(data[i][0:1],data[j][0:1]))
b = target - h_a
print(b)           


#u1,u2 = [1.5,1],[1.5,2]
#diff1,diff2 = np.array([1,1]),np.array([1,1])
#
#while diff1[0]>=0.02 and diff1[1]>=0.02:
#    s1,s2 = [],[]
#    for i in data:
#        
#        dis1 = np.sqrt((i[0] - u1[0])**2 + (i[1] - u1[1])**2)
#        dis2 = np.sqrt((i[0] - u2[0])**2 + (i[1] - u2[1])**2)
#        if dis1 >= dis2:
#            s2.append(i)
#        else:
#            s1.append(i)
#    ns1 = np.array(s1).T    
#    ns2 = np.array(s2).T
#
#    mean1 = np.array([np.mean(ns1[0]),np.mean(ns1[1])])
#    mean2 = np.array([np.mean(ns2[0]),np.mean(ns2[1])])
#    #diff1,diff2 = np.abs(u1) - np.abs(mean1),np.abs(u2) - np.abs(mean2)
#    diff1,diff2 = u1 - mean1,u2 - mean2
#    u1,u2 = mean1,mean2
#    print(len(ns1[0]),len(ns2[0]),u1,u2,sep="\n===================\n")
##plt.plot(x,y,"Dy")
#plt.plot(ns1[0],ns1[1],"r.")
#plt.plot(ns2[0],ns2[1],"g.")
#plt.plot(u1[0],u1[1],"b*")
#plt.plot(u2[0],u2[1],"k*")
#plt.show()