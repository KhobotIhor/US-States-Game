from turtle import Turtle
FONT = ('Arial', 21, 'bold')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()

        self.goto(300, 200)

    def draw(self, score, total):
        self.clear()
        self.pendown()
        self.write(f'{score}/{total}', False, 'center', FONT)
