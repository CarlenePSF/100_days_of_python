# # Target is the number up to which we count
# target = int(input())
# for number in range(1, target + 1):
#   if number % 3 == 0 or number % 5 == 0:  # replace or by and
#     print("FizzBuzz")
#   if number % 3 == 0:  # replace if by elif
#     print("Fizz")
#   if number % 5 == 0:  # replace if by elif
#     print("Buzz")
#   else:
#     print([number])  # remove the brackets

target = int(input("Enter a number: "))

for number in range(1, target + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
