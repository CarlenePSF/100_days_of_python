# 1st input: enter height in meters e.g: 1.65
height = input("what is your height in metters? ")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("What is your weight in kg? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
num_height = float(height)
num_weight = float(weight)

bmi = num_weight/num_height**2


if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
