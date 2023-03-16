# print("Izpildi testu!")

# Q1= int(input("Cik ir 2+4? Atbilde: "))
# if Q1 == 6:
#     print("Pareizi!")
# else:
#     print("Nepareizi!")
# print()
# Q2 = str(input("Kā sauc ģeometrisku figūru, kurai ir 3 malas? Atbilde: "))
    
# if Q2 == "Trijstūris":
#     print("Pareizi!")
# else:
#     print("Nepareizi!")
# print()
# Q3 = int(input("Cik nedēļā ir dienu? Atbilde: "))

# if Q3 == 7:
#     print("Pareizi!")
# else:
#     print("Nepareizi!")

# user_answers = [str(Q1), Q2, str(Q3)]

# print()
# print("Tavas atbildes: ")
# for i, x in enumerate(user_answers):
#     print(f"Jautājums {i + 1}: {x}")

# Right_answers = [6, "Trijstūris", 7]

# print()
# print("Pareizās atbildes: ")
# for i, x in enumerate(Right_answers):
#     print(f"Jautājums{i + 1}: {x}")

#____________________________________________________________

# def check_answer(user_input, right_answer):
#     if user_input == right_answer:
#         print("Pareizi!")
#         return 1
#     else:
#         print("Nepareizi!")
#         return 0

# Q1 = int(input("Cik ir 2+4? Atbilde: "))
# num_correct = check_answer(Q1, 6)

# Q2 = str(input("Kā sauc ģeometrisku figūru, kurai ir 3 malas? Atbilde: "))
# num_correct += check_answer(Q2, "Trijstūris")

# Q3 = int(input("Cik nedēļā ir dienu? Atbilde: "))
# num_correct += check_answer(Q3, 7)

# print(f"Jūs atbildējāt pareizi uz {num_correct} no 3 jautājumiem.")

# num_questions = 3
# num_correct = 0

# while num_questions > 0:
#     Q = int(input("Cik ir 2+4? Atbilde: "))
#     num_correct += check_answer(Q, 6)
#     num_questions -= 1

# print(f"Jūs atbildējāt pareizi uz {num_correct} no 3 jautājumiem.")

#------------------------------------------------------------

# def check_answer(user_input, right_answer):
#     if user_input == right_answer:
#         print("Pareizi!")
#         return 1
#     else:
#         print("Nepareizi!")
#         return 0

# questions = [
#     ("Cik ir 2+4?", 6),
#     ("Kā sauc ģeometrisku figūru, kurai ir 3 malas?", "Trijstūris"),
#     ("Cik nedēļā ir dienu?", 7)
# ]

# num_questions = len(questions)
# num_correct = 0

# while num_questions > 0:
#     question, answer = questions[num_questions - 1]
#     print(f"Jautājums {num_questions}: {question}")
#     print("Izvēlēties: (a) atbildēt (s) pārskaitīt (p) parādīt pareizās atbildes")
#     choice = input("Izvēle: ")
#     if choice == "a":
#         Q = int(input("Atbilde: "))
#         num_correct += check_answer(Q, answer)
#         num_questions -= 1
#     elif choice == "s":
#         num_questions -= 1
#     elif choice == "":
#         break







 










