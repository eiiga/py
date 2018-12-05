import numpy as np
from sklearn import linear_model

# sklearnを使用して回帰式の係数と切片を求める

lr = linear_model.LinearRegression()

# (1)
x = np.array([[0], [2], [3], [5], [6], [7], [9], [11]])
y = np.array([1.5, 1.7, 2.1, 2.2, 2.8, 2.9, 3.2, 3.7])

lr.fit(x, y)

# 係数
print(lr.coef_)

# 切片
print(lr.intercept_)

# (2)
a = np.array([[-2.1, -3.6], [-1.4, 3.1], [0.1, -2.7], [0.8, 1.8], [1.7, -0.5], [3.2, 4.1], [5.7, -1.9], [6.2, 5.2]])
b = np.array([-6.8, 12.2, -8.3, 3.6, -4.8, 5.8, -17.1, 3.1])

lr.fit(a, b)

# 係数
print(lr.coef_)

# 切片
print(lr.intercept_)

# (3)
c = np.array([[-3.4, 5.1, 4.1], [-2.2, 3.7, -3.4], [-1.3, -1.6, 2.6], [0.4, 7.3, -1.4], [1.4, -6.1, -3.6], \
              [2.9, 4.2, 3.5], [4.6, 3.9, 2.9], [6.1, 2.5, -1.1]])
d = np.array([32.5, 16.1, 2.8, 19.1, -27.1, 4.8, -3.5, -17.5])

lr.fit(c, d)

# 係数
print(lr.coef_)

# 切片
print(lr.intercept_)