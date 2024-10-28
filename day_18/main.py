from turtle import Turtle, Screen


joy = Turtle()
joy.shape("turtle")
joy.color("blue")

screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor('white')
screen.exitonclick()

for _ in range(4):
    joy.forward(100)
    joy.left(90)