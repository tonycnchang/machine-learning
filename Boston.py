# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 09:18:12 2019

@author: lenovo
"""
import matplotlib as mpl
import numpy as np
from sklearn.datasets import load_boston
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Lasso, Ridge
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt

boston = load_boston()
x = boston.data
y = boston.target.astype("int")
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=1)

N = len(y_test)

alpha_can = np.logspace(-3, 2, 10)
#boston_model = LogisticRegression(multi_class="multinomial",penalty="l2",solver="lbfgs")
boston_model = LogisticRegression(penalty="l2",solver="lbfgs")
price_model = GridSearchCV(boston_model,param_grid={'alpha': alpha_can},cv=5)
boston_model.fit(x_train,y_train)

y_hat = boston_model.predict(x_test)

xx = range(N)

y_hat1 = np.sort(y_hat)
y_test1 = np.sort(y_test)

plt.plot(xx,y_hat,"ro")
plt.plot(xx,y_test,"g*")
plt.show()


