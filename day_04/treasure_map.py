print("Hiding your treasure! X marks the spot.")

line1 = ["A1","B1","C1"]
line2 = ["A2","B2","C2"]
line3 = ["A3","B3","C3"]

map = [line1, line2, line3]
print(f"{line1}\n{line2}\n{line3}")


position = input("Where do you want to put the treasure?")

# Write your code below this row 👇
row = int(position[1])
column = position[0]

if column == "A":
    map[row-1][0] = "X"
if column == "B":
    map[row-1][1] = "X"
if column == "C":
    map[row-1][2] = "X"




# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")