import numpy as np

# arr = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])

# print(arr)
# print(arr.shape)
# print(arr[:,0])

# arr = np.loadtxt("data/matrix.csv", delimiter=",", dtype=int)

# print(arr)
# print(arr.shape)

# arr = np.loadtxt("data/matrix_tab.txt", dtype=int)
# print(arr)

# arr = np.loadtxt("data/data_skiprow.txt", comments="%", skiprows=2)
# print(arr)

# 只讀某幾欄：usecols

# arr = np.loadtxt("data/matrix_tab.txt", usecols=(0, 2))
# print(arr)

# 每欄分開讀：unpack=True

# x, y, z = np.loadtxt("data/matrix_tab.txt", unpack=True)

# print(x)
# print(y)
# print(z)

# 只讀部分行：max_rows
# arr = np.loadtxt("data/matrix_tab.txt", max_rows=2)
# print(arr)

# 保證至少二維：ndmin
# arr = np.loadtxt("data/data_onerow.txt", ndmin=2)
# print(arr.shape)
# print(arr)

# arr = np.genfromtxt("data/data_nan.txt",
#                      filling_values=np.nan,
#                      names=True)
# print(arr)

# 寫檔 np.savetxt()
# arr = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])

# # %d: int, %.4f: float
# np.savetxt("data/out.txt", arr, fmt="%d")
# np.savetxt("data/out.txt", arr, fmt="%.4f")
# np.savetxt("data/out.csv", arr, fmt="%.6f", delimiter=",")
# np.savetxt("data/out.csv", arr, fmt="%.6f", delimiter=",", header="x y z", comments="")
# np.savetxt("data/out.txt", arr, fmt="%.4f", footer="end", comments="# ")

arr = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

np.savetxt("data/out.txt", arr, fmt="%d")