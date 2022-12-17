from turtle import Screen,Turtle
from snake import Snake
from food import Food
from result import Scoreboard
import time
s=Screen()
s.tracer(0)
s.listen()
sn=Snake()
s.onkey(sn.up, "Up")
s.onkey(sn.right,"Right")
s.onkey(sn.left,"Left")
s.onkey(sn.down,"Down")
score=Scoreboard()
s.setup(600, 600)
s.bgcolor("black")

fd=Food()
game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)
    sn.move_snake()
    for a in sn.segment[1:]:
        if sn.head.distance(a)<18:
            sn.reset_game()
            score.reset_ever()
    if sn.head.distance(fd)<=18:
        fd.clear()
        score.update_score()
        fd.random_position()
        sn.extra_segment()

    if sn.head.xcor()>285 or sn.head.xcor()<-285 or sn.head.ycor()>285 or sn.head.ycor()<-285:
        score.reset_ever()
        sn.reset_game()





















s.exitonclick()

