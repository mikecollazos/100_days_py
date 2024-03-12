from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90.0
DOWN = 270.0
LEFT = 180.0
RIGHT = 0.0


class Snake():
    def __init__(self):
        self.snake_list= []
        #creates starting point snake with 3 segments
        self.create_snake()
        self.head = self.snake_list[0]

    def move(self):
        #Last sname segment will move in same direction of next segment
        for seg_num in range(len(self.snake_list)-1, 0, -1):
            new_x = self.snake_list[seg_num - 1].xcor()
            new_y = self.snake_list[seg_num - 1].ycor()
            self.snake_list[seg_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def create_snake(self):
        starting_x_axis = 0
        for i in range(1,4):
            i = Turtle(shape="square")
            i.color("white")
            i.penup()
            self.snake_list.append(i)
            i.setx(starting_x_axis)
            starting_x_axis+= -20

    def add_segment(self, position):
        i = Turtle(shape="square")
        i.color("white")
        i.penup()
        i.goto(position)
        self.snake_list.append(i)

    def reset(self):
        for segment in self.snake_list:
            segment.goto(1000,1000)
        self.snake_list.clear()
        self.create_snake()
        self.head = self.snake_list[0]


    def extend(self):
        self.add_segment(self.snake_list[-1].position())


    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)


    