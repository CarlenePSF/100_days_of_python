"""
Example of a 'searching algorithm' to find the highest score.
"""
# Input a list of student scores
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# Write your code below this row 👇

max_score = 0

# iterates itens by the index order
for score in student_scores:
    if score > max_score:
        max_score = score


print(f"The highest score in the class is: {max_score}")
