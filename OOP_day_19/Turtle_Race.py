from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400, startx=250, starty= 350)
screen.colormode(255)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a Color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
i = 0
y_axis = -100

for color in colors:
    color = Turtle(shape="turtle")
    color.color(colors[i])
    color.penup()
    color.setposition(-230, y_axis)
    i += 1
    y_axis += 30
    turtle_list.append(color)

if user_bet:
    is_race_on = True

while is_race_on:
    finish_line = 220.0
    for turtle in turtle_list:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        turtle_pos = (turtle.position())[0]
        if turtle_pos >= finish_line:
            winning_turtle = (turtle.color())[0]
            is_race_on = False
            if user_bet.lower() == str(winning_turtle):
                print(f"You Bet Correct. {winning_turtle} turle Won!")
            else:
                print(f"You Bet Wrong. {winning_turtle} turle Won!")

screen.exitonclick()