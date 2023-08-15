from turtle import Turtle
turtle = Turtle()
STARTING_POSITION = (150, -280)
STARTING_POSITION2 = (-150, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)
        self.y_move = 10

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def has_won(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_starting_position(self):
        self.goto(STARTING_POSITION)


class Player2(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION2)
        self.left(90)
        self.y_move = 10

    def go_up(self):
        self.forward(MOVE_DISTANCE)


