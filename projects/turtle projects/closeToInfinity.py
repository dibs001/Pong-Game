import turtle
import math
t=turtle.Turtle()
t.color("dark blue", "yellow")
t.speed(20)
t.begin_fill()
for i in range(2000):
    t.fd(10)
    t.lt(math.sin(i/10)*25)
    t.lt(20)
    
t.end_fill()
turtle.done()