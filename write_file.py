import numpy as np

with open("data/output.txt", "w", encoding="utf-8") as f:
    f.write("Hello\n")
    f.write("World\n")

names = ["Amy", "Bob", "Cindy"]

with open("data/names.txt", "w", encoding="utf-8") as f:
    for name in names:
        f.write(name + "\n")

data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

with open("data/matrix.txt", "w", encoding="utf-8") as f:
    for row in data:
        line = " ".join(str(x) for x in row)
        print(line)
        f.write(line + "\n")

with open("data/matrix.csv", "w", encoding="utf-8") as f:
    for row in data:
        line = ",".join(str(x) for x in row)
        f.write(line + "\n")

students = [
    {"name": "Amy", "score": 85, "dept": "Physics"},
    {"name": "Bob", "score": 92, "dept": "Math"},
    {"name": "Cindy", "score": 78, "dept": "Chemistry"}
]

with open("data/students.txt", "w", encoding="utf-8") as f:
    for s in students:
        line = f"{s['name']} {s['score']} {s['dept']}"
        f.write(line + "\n")

data = [
    [1, 2, 0.123456789],
    [3, 4, 0.987654321]
]

with open("data/num.txt", "w", encoding="utf-8") as f:
    for row in data:
        line = f"{row[0]} {row[1]} {row[2]:.6e}"
        f.write(line + "\n")