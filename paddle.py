from turtle import Turtle, Screen


class Paddle(Turtle):

    def __init__(self, x_position, y_position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(5, 1)
        self.penup()
        self.goto(x_position, y_position)

    def move_paddle_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_paddle_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)




