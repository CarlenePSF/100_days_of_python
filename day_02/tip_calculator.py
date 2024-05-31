"""
If the bill is $124.56, split between 7 people, with 12% tip
Each person should pay (124.56 + 124.56*12/100)/7 = $19.93
round the result for 2 decimal places
"""

print("Welcome to Tip Calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
people_to_split = int(input("How many people to split the bill? "))

tip_as_percentage = tip / 100
total_tip_amount = tip_as_percentage * bill

total_bill = bill + total_tip_amount
bill_per_person = round(total_bill / people_to_split, 2)

print(f'Each person should pay: ${bill_per_person:.2f}')
