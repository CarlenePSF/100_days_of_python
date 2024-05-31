"""
Life in weeks
"""

age = input("How old are you? ")
years_left = 90 - int(age)
weeks_left = years_left * round(52.1429)

print(f"You have {weeks_left} weeks left.")
