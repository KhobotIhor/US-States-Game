from turtle import Turtle, Screen
import pandas as pd
from state_name import State
from score import Score

data = pd.read_csv('50_states.csv')
states = data['state'].to_list()
total = len(states)

screen = Screen()

screen.bgpic('blank_states_img.gif')
screen.tracer(0)

correct = 0
guessed_states = []
learn = {
    'state': [],
}

while len(guessed_states) < 50:
    state = screen.textinput(f'{correct}/{total} States Guessed', 'Enter State Name:  ').title()
    screen.update()
    if state == 'Exit':
        learn['state'] = [item for item in states if item not in guessed_states]
        pd.DataFrame(learn).to_csv('states_to_learn.csv')
        break
    if state in states:
        x_value = int(data[data['state'] == state]['x'].iloc[0])
        y_value = int(data[data['state'] == state]['y'].iloc[0])
        location = (x_value, y_value)
        State().draw(location, state)
        screen.update()
        if state not in guessed_states:
            guessed_states.append(state)
            correct += 1
        print(guessed_states)
        print(x_value, y_value, state)
    else:
        print('No state found')




screen.exitonclick()
