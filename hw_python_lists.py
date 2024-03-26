
# 1. Python List Transformation

# Task 1:

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort()
grades.reverse()
print(grades)

print("\n")

# Task 2:

for grade in grades:
    grade


added_grades = 0
for grade in range(0, len(grades)):
    added_grades = added_grades + grades[grade]

average_grade = added_grades / len(grades)
print(f"The average for the results today is {average_grade}!")

print("\n")

# Task 3:

for grade in grades:
    if grade < 80:
        print(f"You have failed with a grade of {grade}.")
    else:
        print(f"Congratulations! You passed with a {grade}!")

print("\n \n")

# 2. Advanced List Methods and Identity Operators

# Task 1:


submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

print(list(set(submitted) & set(attended)))

# Task 2:

if submitted == attended:
    print("Yo that's weird they're definitely not the same.")
else:
    print("These lists are not the same.")

# Task 3:
print('\n')

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

for student_att in attended:
    if student_att not in submitted:
        attended.remove(student_att)
print(attended)


print('\n')   
# 3. Advanced Slicing Techniques
    
# Task 1:
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
print(temperatures[7:14])

# Task 2:
temperatures.reverse()

while True:
    for temperature in temperatures:
        if temperature > 100:
            print(temperature)
    break
print('\n')

for temperature in temperatures:
    if temperature > 100:
        print(temperature)
print('\n')
# Task 3: 
print(temperatures[4:9])

print('\n')

# 4. Deep Dive into Python Lists

# Task 1:

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]


for student in students:
    index = students.index(student)
    if grades[index] < 80:
        ordered_list = student, grades[index], activities[index]
        print(ordered_list)
print('\n')
# Task 2 & 3:
        
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]


for student in students:
    index = students.index(student)
    if grades[index] > 80:
        students_approved = student, grades[index], activities[index]
        print(students_approved)

