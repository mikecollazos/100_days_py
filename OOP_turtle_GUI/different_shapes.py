from turtle import Turtle, Screen



tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.pensize(8)

screen = Screen()
screen.setup(width=700, height=600)



"""Creates different shapes """
for i in range(3,10):
    for e in range(0,i):
        degrees = 360 / i
        tim.forward(100)
        tim.left(degrees)
        #tim.color(random.choice(colors))
    
"""Pen up and pen down """
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)   
#     tim.pendown()


screen.exitonclick()

