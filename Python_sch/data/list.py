name = "Anna"  # string
age = 17  # integer
height = 1.68  # floating
has_laptop = True  # boolean

# print(name, "is", age, "years old")
# print(f"{name} is {age} years old")

names = ["Anna", "Oskars", "Jenifer", "Anna", "Miks"]
ages = [17, 18, 18, 15, 14]
# loop = cikls

indexes = range(len(names))

for index in indexes:
    print(f"{names[index]} is {ages[index]} years old")
