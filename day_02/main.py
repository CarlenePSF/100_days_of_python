"""
1 - Data Types

# strings - inside double quote "" or single quote ''.

print("Hello"[0])
print("Hello"[4])

# concatenate strings - They are not numbers in a mathematical sense.
print("123" + "345")
print("Hello, " + "world!")


# Integer - Number in a mathematical sense accept sum, subtraction, multiplication, division.

print(123+345)

# Flot - numbers that are seperated into an integer part and decimal part separated by a dot (.)

print(3.14159)

# Boolean - True or False
print(True)
print(False)

# underscore makes the numbers mre readable
print(734_529.678)  # still a float
print(100_000_000)  # still an integer


2 - Type error, Type checking and Type conversion  

# print(len(123))  # TypeError: object of type 'int' has no len()

# In the example below We'll get an error, because we cannot concatenate strings and integers,
# which are different data types
num_char = len(input("What is your name?"))
# print('Your name has ' + num_char + ' characters.')  # TypeError: can only concatenate str (not "int") to str

# type checking with builtin type function
print(type(num_char))

# converting integer data into a string
new_num_char = str(num_char)
print('Your name has ' + new_num_char + ' characters.')

a = str(123)
print(a, type(a))

b = int(a)
print(b, type(b))

c = float(b)
print(c, type(c))


print(3+5)
print(7-4)
print(3*2)
print(6/3)
print(2**3)

# PENDAS order:
# first - parenthesis ()
# second - exponential **
# third -  multiplications * or division /
# fourth - sum + or difference -

print(3*3 + 3/3 - 3)
print(3*(3+3)/3 - 3)
"""

# built in round function
print(round(8/3))
print(round(8/3, 3))
print(8//3)


# use the same variable
result = 4/2
print(result)  # here the print value will be 2
result /= 2  # takes the values of 2 and divided again by 2
print(result)  # will print 1 because 2/2=1


score = 0  # score is set to zero
# user score a point
score += 1  # use the initial value of score and add one to update its value
print(score)  # will print one

# F-string
score = 0
height = 1.9
isWinning = True

print(f'Your score is {score} and your height is {height}. You are winner: {isWinning}')


