from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)
screen.bgcolor("black")

def rand_color():
    for rando in range(0,3):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb = (r, g, b)
    return rgb

for x in range(120):

    tim.speed("fastest")
    tim.width(1)
    tim.right(3)
    tim.pencolor(rand_color())
    tim.circle(100)
    
    


screen.exitonclick()
