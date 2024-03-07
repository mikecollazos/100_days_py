from turtle import Turtle, Screen
import random


tim = Turtle()
tim.pensize(2)
tim.hideturtle()

screen = Screen()
screen.setup(width=700, height=700)
screen.colormode(255)

color_list = [(253, 248, 252), (235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]

tim.penup()
tim.setposition(-300.00, -300.00)

def horizontal():
    for i in range(8):
        tim.dot(20, random.choice(color_list))
        tim.forward(75)

y_axis = -300.00
for i in range(8):
    horizontal()
    y_axis+=75
    tim.setposition(-300.00, y_axis)

screen.exitonclick()