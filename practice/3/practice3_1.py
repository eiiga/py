import numpy as np

# それぞれの逆行列を求める

# (1)
A = np.array([[3, -2], [4, 5]])

print(np.linalg.inv(A))

# (2)
B = np.array([[1, -3, 4], [-2, 5, 3], [2, -1, 0]])

print(np.linalg.inv(B))

# (3)
C = np.array([[-1, 5, 2, -3], [0, 3, -1, 4], [2, -3, 0, -5], [-4, 2, 3, 1]])

print(np.linalg.inv(C))
