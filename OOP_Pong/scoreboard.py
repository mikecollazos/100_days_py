from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.sety(230)
        self.color("white")
        self.penup
        self.left_score = 0
        self.right_score = 0
        self.write((f"Score: \n {self.left_score} | {self.right_score} "), False, align="center", font=('Arial', 16, 'normal'))

    def update_score(self, paddle):
        if paddle.lower() == "left":
            self.left_score += 1
        if paddle.lower() == "right":
            self.right_score += 1       
        self.clear()
        self.write((f"Score: \n {self.left_score} | {self.right_score}"), False, align="center", font=('Arial', 16, 'normal'))
    
    def game_over(self):
        self.goto(0,0)
        self.write(("Game Over"), False, align="center", font=('Arial', 16, 'normal'))

        

