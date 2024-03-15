import turtle
import os
import pandas
from statemanager import StateManager

#make sure path is relative to script
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

screen = turtle.Screen()
screen.setup(width=800, height=600, startx=250, starty= 350)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

statemanager = StateManager()

answer_state = (screen.textinput(title = "Guess the State", prompt="What's another state's name?")).title()

df = pandas.read_csv("50_states.csv")
state_series = df["state"]

score = 0
#loop question game

while len(statemanager.guess_list["state"]) < 50:
    if answer_state == "Exit":
        # missing_states = []
        # for state in state_series:
        #     if state not in statemanager.guess_list["state"]:
        #         missing_states.append(state)
        """list comprehension"""
        missing_states = [state for state in state_series if state not in statemanager.guess_list["state"]]
        new_df = pandas.DataFrame(missing_states)
        new_df.to_csv("states_to_learn.csv")
        break

    if answer_state in state_series.values:
        print("correct")
        state_x = df[state_series == answer_state].x.item()
        state_y = df[state_series == answer_state].y.item()
        statemanager.update_state(answer_state, state_x, state_y)
        score += 1

    else: 
        print("wrong")
    
    answer_state = (screen.textinput(title = f"{score}/50 States Correct", prompt="What's another state's name?")).title()



screen.mainloop()

