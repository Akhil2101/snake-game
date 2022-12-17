from turtle import Turtle
import random

x_cordinate = [0, -20, -40]
all_snake = []


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for a in range(0, 3):
            t = Turtle("turtle")
            t.penup()
            t.color("white")
            t.goto(x_cordinate[a], 0)
            self.segment.append(t)
    def extra_segment(self):
        t = Turtle("turtle")
        t.penup()
        t.color("white")
        t.goto(self.segment[-1].position())
        self.segment.append(t)
    def reset_game(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]


    def move_snake(self):
        for seg in range(len(self.segment)-1,0,-1):
            x=self.segment[seg-1].xcor()
            y=self.segment[seg-1].ycor()
            self.segment[seg].goto(x,y)
        self.head.forward(20)

    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)
    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)
    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)
    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)

