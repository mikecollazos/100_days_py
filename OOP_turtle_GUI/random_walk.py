from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.pensize(8)

screen = Screen()
screen.setup(width=700, height=600)
screen.colormode(255)

direction = [0, 90, 180, 360]

for i in range(1000):
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    tim.pencolor(r, g, b)
    #angle = int(random.random() * 360)
    angle = int(random.choice(direction))
    steps = int(random.random() * 50)
    tim.right(angle)
    tim.fd(steps)

screen.exitonclick()




