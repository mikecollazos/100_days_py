from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.sety(260)
        self.color("white")
        self.score = 0
        self.write((f"Score: {self.score}"), False, align="center", font=('Arial', 16, 'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write((f"Score: {self.score}"), False, align="center", font=('Arial', 16, 'normal'))
    
    def game_over(self):
        self.goto(0,0)
        self.write(("Game Over"), False, align="center", font=('Arial', 16, 'normal'))

        

