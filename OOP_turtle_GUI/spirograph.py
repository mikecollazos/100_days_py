from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.pensize(1)
tim.speed("fastest")

screen = Screen()
screen.setup(width=700, height=600)
screen.colormode(255)



# direction = [0, 90, 180, 360]

for i in range(50):
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    tim.pencolor(r, g, b)
    tim.circle(100)
    tim.right(10)

screen.exitonclick()




