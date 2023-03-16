# import json

# file = open("looping-through-json/students.json", "r")
# data = json.load(file)
# file.close()

# for s in data["Students"]:
#   print(f"{s['FirstName']} {s['LastName']} ({s['Grade']})")

import json

file = open("looping-through-json/students.json", "r")
data = json.load(file)
file.close()

grades_sum = 0
for s in data["Students"]:
    grades_sum += int(s["Grade"])

print(f"Average grade is {grades_sum / len(data['Students'])} ")

# risinajums 2

grades_list = []
for s in data["Students"]:
    grades_list.append(int(s["Grade"]))

print(f"Average grade is {grades_sum / len(data['Students'])} ")
