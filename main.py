from turtle import Turtle
from turtle import Screen
import random
from data import COLORS

# Function that moves Turtle object.
def move(sides):
    tim.color(COLORS[color])
    angle = 360/sides
    for x in range(sides):
        tim.forward(100)
        tim.right(angle)

# Create Turtle Object named tim and move tim to the top, middle of the canvas
tim = Turtle()
tim.shape('turtle')
tim.penup()
tim.hideturtle()
tim.setposition(-50,400)
tim.showturtle()
tim.pendown()

# Prompt user for the number of shapes they would like drawn
input = int(input("Enter the number of shapes you would like to build: "))

for x in range(3,input+3):
        color = random.randint(0, 478)
        move(x)

# Create Screen object
screen = Screen()
screen.exitonclick()
