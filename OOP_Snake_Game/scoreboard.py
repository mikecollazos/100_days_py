from turtle import Turtle
import os

script_dir = os.path.dirname(os.path.abspath(__file__)) + "/"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.sety(260)
        self.color("white")
        self.score = 0
        with open(f"{script_dir}data.txt") as f:
            self.high_score = f.read()
            if self.high_score == "":
                self.high_score = 0
        self.write((f"Score: {self.score} High Score: {self.high_score}"), False, align="center", font=('Arial', 16, 'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write((f"Score: {self.score} High Score: {self.high_score}"), False, align="center", font=('Arial', 16, 'normal'))
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open(f"{script_dir}data.txt", "w") as f:
            f.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.write((f"Score: {self.score} High Score: {self.high_score}"), False, align="center", font=('Arial', 16, 'normal'))
    
    def game_over(self):
        self.goto(0,0)
        self.write(("Game Over"), False, align="center", font=('Arial', 16, 'normal'))

        

