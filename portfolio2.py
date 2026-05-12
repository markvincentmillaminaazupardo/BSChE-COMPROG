# Portfolio 2: My Exam Grade Checker

# Ask for my exam score
my_score = input("What score did I get on the exam? ")

# Convert the input string to a decimal number so I can compare it
my_score = float(my_score)

# Check my grade using multi-way conditions (if, elif, else)
if my_score >= 90:
    print("Wow, I got an excellent grade!")
elif my_score >= 75:
    print("Nice, I passed the exam!")
else:
    print("Oh no, I need to study harder next time.")
