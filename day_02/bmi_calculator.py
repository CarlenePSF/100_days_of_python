# 1st input: enter height in meters e.g: 1.65
height = input("what is your height in meters? ")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("What is your weight in kg? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
num_height = float(height)
num_weight = float(weight)

bmi = int(num_weight/num_height**2)

print("Your BMI is", str(bmi), ".")
