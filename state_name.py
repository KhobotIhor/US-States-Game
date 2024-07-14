from turtle import Turtle
FONT = ('Arial', 8, 'bold')

class State(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()


    def draw(self, location, state):
        self.goto(location)
        self.pendown()
        self.write(state, False, 'center', FONT)

