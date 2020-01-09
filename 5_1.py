import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Lasso, Ridge,RidgeCV
from sklearn.tree import DecisionTreeRegressor
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
#a = np.arange(0,60,10).reshape(-1,1) + np.arange(6)
#print(a)

x = np.arange(0,6.28,0.1)
y = np.sin(x)
x_test = np.arange(-1,1.5,0.1)
d = np.random.random((1,len(y)))[0]/5
np.random.seed(0)
y = y + d

z = np.stack((x,y))

th = np.array([[np.cos(30),np.sin(30)],[-1*np.sin(30),np.cos(30)]])

data = np.dot(th,z).T

x_train = data[:,0].reshape(-1,1)
y_train = data[:,1].reshape(-1,1)

#model = svm.SVR(kernel='poly', degree=5, C=10)
model = DecisionTreeRegressor(criterion='mse', max_depth=10)
#model = Lasso()
#alpha_can = np.logspace(-3, 2, 10)
#l_model = GridSearchCV(model, param_grid={'alpha': alpha_can}, cv=5)

#l_model = LinearRegression()
model.fit(x_train,y_train)
y_hat = model.predict(x_test.reshape(-1,1))

plt.plot(x_train,y_train,"ro")
plt.plot(x_test,y_hat,"go")
plt.show()