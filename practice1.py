# string
'''
text = " Amy, 85, Physics "

# strip(): 去掉空白
name = "   Amy   "
print(name.strip())

# lower() 和 upper()：統一格式
email = "USER@GMAIL.COM"
print(email.lower())
name = "amy"
print(name.upper())

# replace()：替換內容
text = "Physics-Department"
print(text.replace("-", " "))
price = "$100"
print(price.replace("$", ""))

# split()：切開字串
line = "Amy,85,Physics"
parts = line.split(",")
print(parts)
sentence = "apple banana orange"
print(sentence.split()) # 如果 split() 不給參數，它會用空白切。

# join()：把 list 接回字串
words = ["apple", "banana", "orange"]
text = ", ".join(words)
print(text)

raw_lines = [
    " Amy,85,Physics ",
    "Bob,92,Math",
    " Cindy,78,Chemistry "
]

students = []

for line in raw_lines:
    parts = line.strip().split(",")
    student = {
        "name": parts[0],
        "score": int(parts[1]),
        "dept": parts[2]
    }
    students.append(student)

print(students)
'''

# list comprehension：更簡潔的寫法
scores = [85, 92, 78, 90, 60]
# good_scores = []

# for s in scores:
#     if s >= 80:
#         good_scores.append(s)

# good_scores = [s for s in scores if s >= 80]
# print(good_scores)

# 轉換資料
# new_scores = []
# for s in scores:
#     new_scores.append(s+5)
# new_scores = [s+5 for s in scores]
# print(new_scores)

# students = [
#     {"name": "Amy", "score": 85},
#     {"name": "Bob", "score": 92},
#     {"name": "Cindy", "score": 78},
#     {"name": "David", "score": 90}
# ]

# for s in students:
#     print(s.items())

# names = [s["name"] for s in students]
# print(names)

# top_students = [s for s in students if s["score"] >= 90]
# print(top_students)

# top_names = [s["name"] for s in students if s["score"] >= 90]
# print(top_names)
# sorted_students = sorted(students, key=lambda s: s["score"])
# print(sorted_students)

# print(students)
# print(students[0].keys())
# print(students[0].values())
# print(students[0].items())

names = ["Amy", "Bob", "Cindy"]
scores = [85, 92, 78]

students = []

for name, score in zip(names, scores):
    students.append({"name": name, "score": score})

print(students)
