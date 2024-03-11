from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__(shape = "turtle")
        self.penup()
        self.setpos(STARTING_POSITION)
        self.setheading(90)


    def up(self):
        self.setheading(90)
        self.fd(MOVE_DISTANCE)
    def down(self):
        self.setheading(270)
        self.fd(MOVE_DISTANCE)
    def left(self):
        self.setheading(180)
        self.fd(MOVE_DISTANCE)
    def right(self):
        self.setheading(0)
        self.fd(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)