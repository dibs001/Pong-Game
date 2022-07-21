import turtle
import math
t=turtle.Turtle()
t.color("dark blue", "yellow")
t.speed(20)
t.begin_fill()
for i in range(100):
    t.fd(400)
    t.lt(170)
    t.fd(400)
    
t.end_fill()
turtle.done()