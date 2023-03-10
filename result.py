from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super() .__init__()
        self.score =0
        with open("data.txt") as file:
            self.high_score=int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,275)
        self.write_score()
    def write_score(self):
        self.clear()
        self.write(f"score is {self.score} High score: {self.high_score}",align="center", font=('Courier', 15, 'italic'))
    def update_score(self):
        self.score+=1
        self.write_score()
    def reset_ever(self):
        if self.high_score<self.score:
            self.high_score=self.score
            with open("data.txt",mode="w") as file:
                file.write(f"{self.high_score}")
        self.score=0
        self.write_score()



