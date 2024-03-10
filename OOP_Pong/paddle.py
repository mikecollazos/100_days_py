from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90.0
DOWN = 270.0



class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setpos(coordinates)
        self.shapesize(5, 1, 1)


    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
