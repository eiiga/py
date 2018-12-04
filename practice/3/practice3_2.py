import numpy as np

# 連立方程式を解く

# (1) 2x + 5y - 4z = 9
#     3x - 2y + 6z = 9
#     -x + 3y - 2z = 4

A = np.array([[2, 5, -4], [3, -2, 6], [-1, 3, -2]])
B = np.array([9, 9, 4])

print(np.linalg.inv(A) @ B)

# (2) -a + 3b + 5c + sd = 8
#     4a - 6b + 3c - d = -32
#     3a + 3b -4c + 3d = 26
#     sa - b + 2c -4d = -25

C = np.array([[-1, 3, 5, 2], [4, -6, 3, -1], [3, 3, -4, 3], [2, -1, 2, -4]])
D = np.array([8, -32, 26, -25])

print(np.linalg.inv(C) @ D)
