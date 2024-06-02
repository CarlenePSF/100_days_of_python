"""
# If else statements


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster.")
else:
    print("Sorry, you have to grow taller before you can ride.")

# Nested if else statements

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please, pay $5.")
    elif age <= 18:
        print("Please, pay $7.")
    else:
        print("Please, pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")

"""
# multiple if conditions

print("Welcome to the rollercoaster!")

ticket = 0
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age < 12:
        print("Child tickets are $5.")
        ticket = 5
    elif age <= 18:
        print("Youth tickets are $7.")
        ticket = 7
    else:
        print("Adult tickets are $12.")
        ticket = 12

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        ticket += 3
    print(f"Your final bill is ${ticket}.")
else:
    print("Sorry, you have to grow taller before you can ride.")

