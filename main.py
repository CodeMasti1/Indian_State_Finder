from turtle import Turtle, Screen

import pandas as pd

FONT = ("arial", 10, "normal")

t = Turtle()
screen = Screen()
screen.title("Guess the Indian State")
screen.setup(height=972, width=1180)
image = "2a10d13ef89063732136ae9b4c8d7da6.gif"
screen.addshape(image)
t.shape(image)

states_details = pd.read_csv("mapdata.csv")
states = states_details.State.to_list()
guessed_states = []
missing_states = []
while len(guessed_states) < 29:
    answer = screen.textinput(
        title=f"{len(guessed_states)}/29 guessed states", prompt="Guess a State"
    ).title()
    if answer == "Exit":
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)

        to_be_learn = pd.DataFrame(missing_states)
        to_be_learn.to_csv("states_to_be_learn.csv")
        break
    if answer in states:
        t2 = Turtle()
        t2.ht()
        t2.pu()
        state_data = states_details[states_details.State == answer]
        x_cor = int(state_data.x.iloc[0])
        y_cor = int(state_data.y.iloc[0])
        t2.goto(x_cor, y_cor)
        t2.write(arg=answer, move=False, align="center", font=FONT)
        guessed_states.append(answer)
screen.exitonclick()
