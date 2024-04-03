from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake():
    def __init__(self) -> None:
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_snake(pos)

    def add_snake(self, pos):
        s = Turtle("square")
        s.color("white")
        s.penup()
        s.goto(pos)
        self.snake.append(s)

    def extend(self):
        self.add_snake(self.snake[-1].position())

    def reset(self):
        for segment in self.snake:
            segment.reset()
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].goto(self.snake[i-1].xcor(), self.snake[i-1].ycor())
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
