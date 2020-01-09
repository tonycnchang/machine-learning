# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 13:48:04 2018

@author: lenovo
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn import preprocessing
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import Lasso, Ridge
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

iris = datasets.load_iris()

X,y = iris['data'],iris["target"]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.3,random_state = 1)
z = len(y_test)

#随机森林
cm_light = mpl.colors.ListedColormap(['#A0FFA0', '#FFA0A0', '#A0A0FF'])
cm_dark = mpl.colors.ListedColormap(['g', 'r', 'b'])
for i in range(3):
    for j in range(1,4):
        if j > i:
            model = RandomForestClassifier(n_estimators=10, criterion='entropy', max_depth=3)
            model_tr = model.fit(X_train[ : ,(i,j)],y_train)
            
            # 画图
            N, M = 100, 100  # 横纵各采样多少个值
            x1_min, x1_max = X[:, i].min(), X[:, i].max()  # 第0列的范围
            x2_min, x2_max = X[:, j].min(), X[:, j].max()  # 第1列的范围
            t1 = np.linspace(x1_min, x1_max, N)
            t2 = np.linspace(x2_min, x2_max, M)
            x1, x2 = np.meshgrid(t1, t2)  # 生成网格采样点
            x_show = np.stack((x1.flat, x2.flat), axis=1)
            y_show_hat = model_tr.predict(x_show)
            y_show_hat = y_show_hat.reshape(x1.shape)
            y_test_hat = model.predict(X_test[:,(i,j)]) 
            plt.subplot(2, 3, i+j)
            plt.pcolormesh(x1, x2, y_show_hat, cmap=cm_light)
            plt.scatter(X_test[:, i], X_test[:, j], c=y_test_hat, cmap=cm_dark)
            plt.show()
            c = np.count_nonzero(y_test_hat == y_test)
            #print("X_train=\n" ,X_train)
            print("y_train=\n" ,x1)
            print("正确个数：", c)
            print("正确率：" , c/z*100,"%")
                                                 

"""

#model = Pipeline([
#    ('ss', StandardScaler()),
#    ('DTC', DecisionTreeClassifier(criterion='entropy', max_depth=8))])
#
#model = model.fit(x.reshape(-1,1),y_cal.astype(int))

#poly = preprocessing.PolynomialFeatures(1)
#X = poly.fit_transform(X)
alpha_give = np.logspace(-3,2,10)
#model = Lasso()
model = Ridge()
lo_model = GridSearchCV(model,param_grid = {"alpha":alpha_give},cv = 5)
lo_model.fit(X_train,y_train)

#X_test = poly.fit_transform(X_test)
y_test_hat = lo_model.predict(X_test)
print(y_test_hat)
y_test_hat = np.rint(y_test_hat)
print(y_test_hat)
c = np.count_nonzero(y_test_hat == y_test)
print(c)
print(lo_model.best_params_)
#print(model.coef_)
#print(model.intercept_)
#print(model.get_params())
"""