########### Challenge 4 - Random Walk ########

import turtle
from random import randint, random, choice
from turtle import Turtle, Screen


turtle.colormode(255)
t = Turtle()
t.pensize(7)
t.speed("fastest")
t.screen.title('random-walk')


screen = Screen()

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b

def move_up_or_down(p_y):
    if p_y > p_up:
        # para baixo
        t.setheading(270)
    else:
        # para cima
        t.setheading(90)
    t.forward(30)


def move_right_or_left(p_x):
    if p_x > p_right:
        # para esquerda
        t.setheading(0)
    else:
        # para direita
        t.setheading(180)
    t.forward(30)

def main():
    steps = 100
    i = 0
    j = 0


    while i < steps:
        while j < steps:
            py = random()
            px = random()
            t.pencolor(random_color())

            move_up_or_down(py)
            move_right_or_left(px)
            j += 1
        i += 1


p_up = 0.5
p_right = 0.5
main()
screen.mainloop()


