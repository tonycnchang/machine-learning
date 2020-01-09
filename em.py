# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 16:27:20 2018

@author: lenovo
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

def norm(x,mu,sigma):
    n = (1/(np.sqrt(2*np.pi)*sigma))*np.exp((-1*np.square(x-mu))/(2*np.square(sigma)))
    return n
np.random.seed(0)
#boy = np.random.multivariate_normal()
boy = np.around(np.random.normal(188,5,20),2).T
boy = np.where(boy<155,155,boy)
girl = np.around(np.random.normal(168,3,20),2).T
girl = np.where(girl<145,145,girl)
#y = np.array([True] * 400 + [False] * 100)
data = np.hstack((boy, girl))

mu_boy,mu_girl = 180,160
sigma_boy,sigma_girl = 4,3

pi1 = 0.5
pi2 = 1-pi1
for i in range(3):
    norm1 = norm(data,mu_boy,sigma_boy)
    norm2 = norm(data,mu_girl,sigma_girl)
    
    p_norm1 = pi1*norm1/(pi1*norm1+pi2*norm2)
    p_norm2 = pi2*norm2/(pi1*norm1+pi2*norm2)
    
    new_boy = p_norm1*data
    new_girl = p_norm2*data
    
    mu_boy = np.sum(new_boy)/np.sum(p_norm1)
    mu_girl = np.sum(new_girl)/np.sum(p_norm2)
    
    sigma_boy = np.sum(p_norm1*np.dot((data-mu_boy),(data-mu_boy).T))/np.sum(p_norm1)
    sigma_girl = np.sum(p_norm2*np.dot((data-mu_girl),(data-mu_girl).T))/np.sum(p_norm2)
    print(new_boy)
    print(new_girl)
