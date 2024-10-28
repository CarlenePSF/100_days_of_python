import turtle
from turtle import Turtle, Screen
from random import randint


turtle.colormode(255)
t = Turtle()
t.speed("fastest")
t.screen.title('Spirograph')

screen = Screen()

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def draw_spirograph(size):
    for _ in range(round(360/size)):
        t.pencolor(random_color())
        t.circle(100)
        t.setheading(t.heading() + size)


draw_spirograph(15)
screen.exitonclick()


