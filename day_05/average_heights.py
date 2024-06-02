# Input a Python list of student heights
student_heights = [156, 178, 165, 171, 187]

# Write your code below this row 👇

total_height = 0
number_of_students = 0

for height in student_heights:
    total_height += height
    number_of_students += 1

average_student_height = round(total_height / number_of_students)

print(f"total height = {total_height}")
print(f"number of students = {number_of_students}")
print(f"average height = {average_student_height}")
