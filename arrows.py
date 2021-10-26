from turtle import *
import random as r
import colorsys as col


bgcolor('black')
screen = Screen()
screen.tracer(0, 0)

army = [
    Turtle() for i in range(100)
]
o = 0
for T in army:
    c = col.hsv_to_rgb(o, 1, 1)
    o += 1/100
    T.color(c)
    T.up()
    T.goto(
      r.uniform(-500, 500),
      r.uniform(-500, 500)
    )


def action():
    for i in range(100):
        angle = army[i].towards(
            army[(i+1) % 100]
        )
        army[i].seth(angle)
    for T in army:
        T.forward(3)
    screen.update()
    screen.ontimer(action, 1)


action()
done()
