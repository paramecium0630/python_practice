import numpy as np

# test 1
# x = np.arange(1, 11)

# print(x*x)
# print(x[x>5])
# print(x[x%2 == 0])
# print(np.mean(x))
# print(np.std(x))

# test 2
# A = np.arange(1, 17).reshape(4, 4)

# print(A)
# # print(A[0])
# # print(A[:,1])
# # print(A[0:2,0:2])
# # print(A[-2:,-2:])
# print(np.diag(A))

# test 3
# data = np.array([
#     [1, 1, 0.1],
#     [1, 2, 0.2],
#     [2, 1, 0.3],
#     [2, 2, 0.4],
#     [3, 1, 0.5]
# ])

# # print(data[data[:,0]==data[:,1]])
# # print(data[data[:,0]!=data[:,1]])
# # print(data[data[:,2]>0.25])
# print(data[(data[:,0] == 1) | (data[:,1] == 1)])

# test 4
A = np.array([
    [2, 1],
    [1, 3]
], dtype=float)

b = np.array([1, 2], dtype=float)

# Ax = b
x = np.linalg.solve(A, b)
print(x)