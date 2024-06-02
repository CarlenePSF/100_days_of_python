"""
Calculating the sum of even numbers
"""

target = int(input("Enter a number between 0 and 1000: "))

sum_of_numbers = 0

for number in range(1, target+1):
    if number % 2 == 0:
        sum_of_numbers += number

print(sum_of_numbers)


# Another way
sum_of_numbers = 0

for number in range(2, target+1, 2):
    sum_of_numbers += number

print(sum_of_numbers)
