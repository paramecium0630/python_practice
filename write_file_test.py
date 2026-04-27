import numpy as np

# practice 6

names = ["Amy", "Bob", "Cindy", "David"]

with open("data/write.txt", "w") as f:
    for name in names:
        f.write(name + "\n")

# practice 7 & 8
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

with open("data/matrix_out.txt", "w") as f:
    for line in data:
        row = ",".join(str(x) for x in line)
        f.write(row + "\n")

# practice 9
scores = []
with open("data/scores.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line == "":
            continue
        name, score = line.split()
        row = {"name": name,
               "score": int(score)}
        scores.append(row)
print(scores)

with open("data/top_students.txt", "w") as f:
    for s in scores:
        if s["score"] >= 90:
            f.write(f"{s["name"]} {s["score"]}\n")

# practice 10
student_data = []
with open("data/raw_data.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line == "" or line.startswith("#"):
            continue
        name, score, dept = line.split(",")
        row = {"name": name,
               "score": int(score),
               "dept": dept}
        student_data.append(row)

print(student_data)

average = sum(s["score"] for s in student_data) / len(student_data)

print(average)

with open("data/clean_data.txt", "w") as f:
    for line in student_data:
        f.write(f"{line["name"]} {line["score"]} {line["dept"]}\n")