# Data for girls
girls_names = ["Evelyn", "Jessica", "Somto", "Edith", "Liza", "Madonna", "Waje", "Tola", "Aisha", "Latifa"]
girls_ages = [17, 16, 17, 18, 16, 18, 17, 20, 19, 17]
girls_heights = [5.5, 6.0, 5.4, 5.9, 5.6, 5.5, 6.1, 6.0, 5.7, 5.5]
girls_scores = [80, 85, 70, 60, 76, 66, 87, 95, 50, 49]

# Data for boys
boys_names = ["Chinedu", "Liam", "Wale", "Gbenga", "Abiola", "Kola", "Kunle", "George", "Thomas", "Wesley"]
boys_ages = [19, 16, 18, 17, 20, 19, 16, 18, 17, 19]
boys_heights = [5.7, 5.9, 5.8, 6.1, 5.9, 5.5, 6.1, 5.4, 5.8, 5.7]
boys_scores = [74, 87, 75, 68, 66, 78, 87, 98, 54, 60]

# Combine data for all students
all_students = []
for i in range(len(girls_names)):
    all_students.append([girls_names[i], girls_ages[i], girls_heights[i], girls_scores[i]])
for i in range(len(boys_names)):
    all_students.append([boys_names[i], boys_ages[i], boys_heights[i], boys_scores[i]])

# Print the header
print("{:<10} | {:<3} | {:<6} | {:<5}".format("Name", "Age", "Height", "Score"))
print("-" * 30)

# Print the student data
for student in all_students:
    name, age, height, score = student
    print("{:<10} | {:<3} | {:<6} | {:<5}".format(name, age, height, score))