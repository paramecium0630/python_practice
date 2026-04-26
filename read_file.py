import numpy as np
import pandas as pd

# f.read(): 把整個檔案一次讀進來，變成一個大字串
# utf-8: 文字編碼

############# 單行多列 #############

# 為什麼要用 with
#因為 with 會在區塊結束後自動關檔。
# with open("data.txt", "r", encoding="utf-8") as f:
#     content = f.read() # 全讀
# print(content)
# print(type(content))

# with open("data.txt", "r", encoding="utf-8") as f:
#     content = f.readline() # 讀一行
# print(content.strip())
# print(type(content))

# with open("data.txt", "r", encoding="utf-8") as f:
#     for line in f: # 一行一行讀
#         print(repr(line)) # repr: 將字串裡真正的內容顯示出來 (引號、\n、\t)

# with open("data.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         line = line.strip()
#         print(line)

# name = [] # 存成 list
# with open("data.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         line = line.strip()
#         if line == "":
#             continue
#         name.append(line)
# print(name)

############# 多行多列 #############

# 空白分隔
# data = []
# with open("data_space.txt", "r") as f:
#     for line in f:
#         line = line.strip() # 去掉前後空格
#         if line == "":
#             continue
        
#         parts = line.split() # 拆成不同字串，空白鍵
#         print(parts)
#         row = [float(x) for x in parts]
#         data.append(row)

# data = np.array(data)
# print(data)

# 逗號分隔
# data = []
# with open("data.csv", "r", encoding="utf-8") as f:
#     for line in f:
#         line = line.strip()
#         if line == "":
#             continue

#         parts = line.split(",") # 拆成不同字串，逗號
#         row = [int(x) for x in parts]
#         data.append(row)

# print(data)

# tab分隔
# data = []
# with open("data_tab.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         line = line.strip()
#         if line == "":
#             continue

#         parts = line.split("\t") # 拆成不同字串，tab
#         row = [int(x) for x in parts]
#         data.append(row)

# print(data)

############# 多行多列：字串 + 數字混合 #############

# students = []

# with open("students.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         line = line.strip()
#         if line == "":
#             continue

#         parts = line.split()

#         student = {
#             "name": parts[0],
#             "score": int(parts[1]),
#             "dept": parts[2]
#         }
#         students.append(student)

# print(students[0]["name"])

#### 科學記號、多欄數值檔

data = []

with open("data_num.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line == "":
            continue
        
        parts = line.split()
        row = [int(parts[0]),
               int(parts[1]),
               float(parts[2]),
               float(parts[3])]
        
        data.append(row)

print(data)