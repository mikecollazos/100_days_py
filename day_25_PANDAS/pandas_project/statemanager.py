from turtle import Turtle


class StateManager(Turtle):
    def __init__(self):
        super().__init__()
        self.guess_list = {"state": []}
        self.hideturtle()

    def update_state(self, state,x_cor, y_cor):
        new_state = Turtle()
        new_state.state = state
        new_state.hideturtle()
        new_state.penup()
        new_state.goto(x_cor, y_cor)
        new_state.write(state)
        self.guess_list["state"].append(new_state.state)

