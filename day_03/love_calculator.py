"""
Love calculator
"""
print("The Love Calculator is calculating your score...")
name1 = input('What is your name?')
name2 = input('What is their name?')

combined_names = name1+name2
combined_names = combined_names.lower()

t = combined_names.count('t')
r = combined_names.count('r')
u = combined_names.count('u')
e = combined_names.count('e')

l = combined_names.count('l')
o = combined_names.count('o')
v = combined_names.count('v')

first_digit = t + r + u + e
second_digit = l + o + v + e

print(first_digit)
print(second_digit)

love_score = int(str(first_digit) + str(second_digit))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 < love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
