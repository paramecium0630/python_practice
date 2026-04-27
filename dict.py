
student = {
    "name": "Alice",
    "age": 20,
    "major": "Physics"
}
# student["height"] = 197
major = student.get("height", 197)
# print(student["name"])
# print(student["age"])
# print(major)

# for key, value in student.items():
#     print(key, value)

# dict comprehension
# nums = [1, 2, 3, 4]

# squares = {x: x**2 for x in nums}

# print(squares)

words = ["apple", "banana", "apple", "orange", "banana", "apple"]

count = {}

for word in words:
    if word not in count:
        count[word] = 0
    else:
        count[word] += 1

print(count)