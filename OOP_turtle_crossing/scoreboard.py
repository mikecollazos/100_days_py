from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.score = 0
        self.write((f"Level: {self.score}"), False, align="left", font=FONT)    

    def update_score(self):
        self.score += 1
        self.clear()
        self.write((f"Level: {self.score}"), False, align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(("Game Over"), False, align="center", font=FONT)

        


