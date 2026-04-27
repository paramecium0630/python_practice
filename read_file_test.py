import numpy as np

FILE = 'data/students.txt'

# practice 1
'''
name_list = []
# with open(FILE, "r") as f:
#     for line in f:
#         line = line.strip()
#         name_list.append(line)

# print(name_list)
# print(len(name_list))

with open(FILE, "r") as f:
    name_list = [line.strip() for line in f]

print(name_list)
'''

# practice 2
'''
name_list = []
with open(FILE, "r") as f:
    for line in f:
        line = line.strip()
        if line == "":
            continue
        name_list.append(line)

print(name_list)
'''

# practice 3
'''
lines = []
with open(FILE, "r") as f:
    for line in f:
        line = line.strip().split()
        lines.append([
            int(line[0]),
            int(line[1]),
            int(line[2])
        ])
print(lines)
'''

# practice 4
'''
students = []
with open(FILE, "r") as f:
    next(f)
    for line in f:
        line = line.strip()
        if line == "":
            continue
        
        name, score, dept = line.split()

        student = {"name": name,
             "score": int(score),
             "dept": dept}

        students.append(student)

print(students)

for s in students:
    if s["score"] >= 90:
        print(s["name"])

average = sum(s["score"] for s in students) / len(students)
print(average)
'''

# practice 5
'''
lines = []
with open("data/experiment.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line == "" or line.startswith("#"):
            continue
        line = line.split()
        row = [float(x) for x in line]
        lines.append(row)

print(lines)
'''