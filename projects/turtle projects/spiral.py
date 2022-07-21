import turtle
import math
t=turtle.Turtle()
t.color("dark blue", "yellow")
t.speed(20)
t.begin_fill()
for i in range(2000):
    t.fd(math.sqrt(i))
    t.lt(i%180)    
t.end_fill()
turtle.done()