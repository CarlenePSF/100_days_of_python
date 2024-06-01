print('''
|*******************************************
                  |                  |       
|___________.=""_;=.______________|_________
       ,-"_,=""     `"=.|    |
|______"=._o`"-._        `"=.______________|
         `"=._o`"=._      _`"=._           |
|_______________:=._o "=._."_.-="'"=._______
         __.--" , ; `"=._o." ,-"""-._ ".   |
|_____._"  ,. .` ` `` ,  `"-._"-._   ". '__|
|_____| ;`-.o`"=._; ." ` '`."\` . "-._ /____
      |o;    `"-.o`"=._``  '` " ,__.--o;   |
|_____| ;     (#) `-.o `"=.`_.--"_o.-; ;___|
|__/__|o;._    "      `".o|o_.--"    ;o;____
|____/_"=._o--._        ; | ;        ; ;/___
|__/_____/__"=._o--._   ;o|o;     _._;o;____
|____/______/____"=._o._; | ;_.--"o.--"_/___
|__/_____/______/_____"=.o|o_.--""___/______
|____/______/______/______/______/______/___
|*******************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("You are the middle of a crossroad and you have to choso 'left' of 'right'...\n").lower()

if direction == "right":
    print("Fall in a hole. Game Over!")
else:
    action = input("Do you want to 'swim' or 'wait'?\n").lower()
    if action == "swim" or action == "swin":
        print("You were attacked by a shark. Game Over!")
    else:
        color = input("Which door you choose: red, yellow or blue?\n").lower()
        if color == "red":
            print("You were burned by fire. Game Over!")
        elif color == "yellow":
            print("You found the treasure.You Win!")
        else:
            print("Zombies attacked you. Game Over!")
