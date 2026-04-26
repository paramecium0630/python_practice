import numpy as np
import pandas as pd

# f.read(): 把整個檔案一次讀進來，變成一個大字串
# utf-8: 文字編碼

# 為什麼要用 with
#因為 with 會在區塊結束後自動關檔。
# with open("Ktaudir.dat", "r", encoding="utf-8") as f:
#     content = f.read() # 全讀
# print(content)
# print(type(content))

# with open("Ktaudir.dat", "r", encoding="utf-8") as f:
#     content = f.readline() # 一行一行讀
# print(content)
# print(type(content))

# with open("Ktaudir.dat", "r", encoding="utf-8") as f:
#     for line in f:
#         print(repr(line)) # repr: 將字串裡真正的內容顯示出來 (引號、\n、\t)

# with open("Ktaudir.dat", "r", encoding="utf-8") as f:
#     for line in f:
#         line = line.strip()
#         print(line)

name = []
with open("Ktaudir.dat", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line == "":
            continue
        name.append(line)
print(name)

