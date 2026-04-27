import numpy as np

# numpy.ndarray

'''
NumPy 的核心優點是：
比 Python list 快很多。
可以直接做向量、矩陣運算。
支援線性代數、隨機數、統計量、檔案讀寫。
'''

# 1. 建立 array
a = np.array([1, 2, 3])
# print(a)
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# print(A)
# print(A.shape)
# print(A.ndim)
# print(A.size)
# print(A.dtype)

# 2. 建立特殊 array
# n0 = np.zeros(5)
# print(n0)
# n1 = np.zeros((3, 4))
# print(n1)
# n2 = np.ones((2, 3))
# print(n2)
# n3 = np.full((2, 3), 7)
# print(n3)

# n4 = np.arange(0, 10, 2.5) # 等差數列
# print(n4)

# x = np.linspace(0, 1.0, 5)
# print(x)

# I = np.eye(3) # 單位矩陣
# print(I)

# 3. NumPy array 和 Python list 的差別

# a = [1, 2, 3]
# print(a + a)
# a = np.array([1, 2, 3])
# print(a + a)

# x = np.array([1, 2, 3, 4])

# print(x + 1)
# print(x * 2)
# print(x ** 2)
# print(np.sqrt(x))

# x = np.array([10, 20, 30, 40, 50])
# print(x[0])
# print(x[1])
# print(x[-1])

# Boolean indexing：資料篩選核心技巧
# x = np.array([1, 5, 8, 2, 10])

# mask = x > 5
# print(x[mask])
# print(x[(x>2) & (x<8)])

# data = np.array([
#     [1, 1, 0.9833382177E-04, 0.9833382177E-04],
#     [1, 2, 0.9003827892E-05, 0.9075737893E-05],
#     [1, 3, 0.8605172189E-05, 0.8715865821E-05],
#     [2, 2, 0.1234567890E-04, 0.2222222222E-04]
# ])
# same = data[data[:, 0] != data[:, 1]]
# print(same)

# np.where

# x = np.array([1, 5, 8, 2, 10])
# y = np.where(x > 5, 100, 0)
# print(y)

# array shape

# x = np.arange(12)
# print(x)
# A = x.reshape(3, 4)
# B = A.ravel()
# print(A)
# print(B)

# x = np.array([1, 2, 3])
# print(x.shape)
# x_col = x[:, np.newaxis]
# x_row = x[np.newaxis, :]
# print(x_col)
# print(x_row)
# print(x_col.shape)
# print(x_row.shape)

# 解線性方程
# A = np.array([
#     [2, 1],
#     [1, 3]
# ])

# b = np.array([1, 2])
# # Ax = b
# x = np.linalg.solve(A, b)
# print(x)

# # inverse matrix
# A_inv = np.linalg.inv(A)
# print(A_inv)

# # eigenvalue, eigenvector
# eigvals, eigvecs = np.linalg.eig(A)
# print(eigvals, eigvals)
# eigvals, eigvecs = np.linalg.eig(A_inv)
# print(eigvals, eigvals)
# eigvals, eigvecs = np.linalg.eigh(A) # for symmetric matrices
# print(eigvals, eigvals)
# det = np.linalg.det(A)
# trace = np.trace(A)
# print(det, trace)

# random number
# rng = np.random.default_rng(seed=123) # uniform random numbers
# x = rng.random(5)
# print(x)

# eta = rng.normal(loc=0.0, scale=1.0, size=10) # loc: mean, scale: sd, size: shape
# print(eta)

# N = 5
# dt = 0.01
# sigma = 2.0
# sigma_vec = np.array([1.0, 2.0, 0.5, 1.5, 3.0]) # diagonal
# rng = np.random.default_rng(123)
# noise = np.sqrt(sigma_vec * dt) * rng.normal(size=N)
# print(noise)

# 常見資料處理範例
# data = np.array([
#     [1, 1, 0.9833382177E-04, 0.9833382177E-04, 0.7033884686E-04],
#     [1, 2, 0.9003827892E-05, 0.9075737893E-05, 0.8920109504E-05],
#     [1, 3, 0.8605172189E-05, 0.8715865821E-05, 0.8461999722E-05],
#     [2, 2, 0.1111111111E-04, 0.2222222222E-04, 0.3333333333E-04],
# ])

# i = data[:, 0].astype(int)
# j = data[:, 1].astype(int)
# value = data[:, 2]
# diag_data = data[data[:, 0] == data[:, 1], 3]
# offdiag_data = data[data[:, 0] != data[:, 1], 3]
# print(offdiag_data)

# 排序
# x = np.array([5, 2, 8, 1])
# np.sort(x)
# idx = np.argsort(x)[::-1]
# print(x)
# print(idx)

# 