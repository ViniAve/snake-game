from turtle import Turtle


class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", False, "center", ("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", ("Courier", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
