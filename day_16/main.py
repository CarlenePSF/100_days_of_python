"""
Object-oriented programming

class - waiter

objects - can be multiple
our waiters are :
    janny
    jack


attributes - what it has - "variables"
    is_holding_plate = True
    tables_responsible = [4, 5, 6]

methods - what it does - "functions"
    take_order(table, order)

    take_payment(table, payment)


# Example
class WaiterBlueprint():
    ...

from waiter import Waiter

jack = WaiterBlueprint()
"""

from turtle import Turtle, Screen

joy = Turtle()  # object
print(joy)  # the memory address of our object
joy.shape('turtle')  # method
joy.color('blue')  # method

# drawing a square
joy.forward(100)  # method
joy.left(90)
joy.forward(100)
joy.left(90)
joy.forward(100)
joy.left(90)
joy.forward(100)


my_screen = Screen()  # object
print(my_screen.canvheight)  # atribute
my_screen.exitonclick()  # a method











