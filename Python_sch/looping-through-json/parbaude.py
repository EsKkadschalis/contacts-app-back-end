import json

file = open("looping-through-json/test.json", "r")
data = json.load(file)
file.close()

# for t in data["qwerty"]:
#     print(f"{t['Age']}")              


