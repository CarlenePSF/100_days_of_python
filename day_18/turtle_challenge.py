from random import randint, random, choice
from turtle import Turtle, Screen


t = Turtle()
screen = Screen()

t.screen.title('Turtle Challenge')

colours = [
    "CornflowerBlue", "DarkOrchid",
    "IndianRed", "DeepSkyBlue",
    "LightSeaGreen", "wheat",
    "SlateGray", "SeaGreen"
]

########### Challenge 1 - Draw a square ########
for _ in range(4):
    t.forward(100)
    t.left(90)

########### Challenge 2 - Draw a Dashed Line ########

t.color("blue")
for _ in range(15):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()

########### Challenge 3 - Draw Shapes ########

def form(number_of_sides):
    for _ in range(number_of_sides):
        angle = 360 / number_of_sides
        t.forward(100)
        t.right(angle)


i = 3
while i < 11:
    t.color(choice(colours))
    form(i)
    i += 1

screen.mainloop()





