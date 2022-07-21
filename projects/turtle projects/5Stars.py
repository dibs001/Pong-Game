import turtle
import math
t=turtle.Turtle()
t.getscreen().bgcolor("cyan")
t.speed(50) 
def star(turtle,size):
    if size<=10:
        return
    else:
        for i in range(5):
            t.fd(size)
            star(turtle,size/2)
            t.lt(216)

star(t,200)
turtle.done()