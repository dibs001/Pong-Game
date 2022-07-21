import turtle#importing turtle module
import winsound #importing sound module
window=turtle.Screen()
window.title("Pong by Dibs")
window.bgcolor("yellow")
window.setup(width=800,height=600)
window.tracer(0)#speeds up the game;(0) coz automatic screen updates are off;(1) to turn on the automatic screen updates

# Paddle a
paddle_a=turtle.Turtle()
paddle_a.speed(0)#speed set to 'fastest'(0 being fastest and 1 being slowest)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_len=1,stretch_wid=5)#by default shape is 20 by 20 pixels
paddle_a.penup()#if pendown() then it'll keep drawing
paddle_a.goto(-350,0)
# Paddle b
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)#x,y coordinates

# Ball
ball=turtle.Turtle()#ball is initially 20 by 20 pixels
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0,0)
ball.dx=0.15
'''the x-increment or y-increment (the amount by which the turtle's xcor or ycor would change) 
if the turtle were to take one step forward in its current heading.Here the ball moves by 0.1 pixels'''
ball.dy=0.15
#Score
score_a=0
score_b=0
# Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0\tPlayer B: 0",align="center", font=("Cursive",23,"normal"))
# function
def paddle_a_up():
    y=paddle_a.ycor()#stores y coordinate
    y+=30#speed with which the paddle_a moves up
    paddle_a.sety(y)
def paddle_a_down():
    y=paddle_a.ycor()
    y-=30#speed with which the paddle_a moves down
    paddle_a.sety(y)
def paddle_b_up():
    y=paddle_b.ycor()
    y+=30
    paddle_b.sety(y)
def paddle_b_down():
    y=paddle_b.ycor()
    y-=30
    paddle_b.sety(y)
# keyboard binding
window.listen()#listen for keyboard i/ps
window.onkeypress(paddle_a_up,"w")
window.onkeypress(paddle_a_down,"s")
window.onkeypress(paddle_b_up,"Up")
window.onkeypress(paddle_b_down,"Down")
# main game loop
while True:
    window.update()
    # move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    # border checking
    if ball.ycor()>290:
        ball.sety(290)
        winsound.PlaySound("ballhit.wav",winsound.SND_ASYNC)
        ball.dy*=-1#reverses direction of the ball(2*-1=-2)
    if ball.ycor()<-280:
        ball.sety(-280)
        winsound.PlaySound("ballhit.wav", winsound.SND_ASYNC)
        ball.dy*=-1
    if ball.xcor()>390:
        ball.goto(0,0)
        winsound.PlaySound("ballhit.wav", winsound.SND_ASYNC)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("Player A: {}\tPlayer B: {}".format(score_a,score_b), align="center", font=("Verdana", 23, "normal"))
    if ball.xcor()<-390:
        ball.goto(0,0)
        winsound.PlaySound("ballhit.wav", winsound.SND_ASYNC)
        ball.dx*=-1
        score_b +=1
        pen.clear()
        pen.write("Player A: {}\tPlayer B: {}".format(score_a,score_b), align="center", font=("Verdana", 23, "normal"))
    # paddle and ball collisions
    if (ball.xcor()>335 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+60 and ball.ycor()>paddle_b.ycor()-60):
        ball.setx(335)
        winsound.PlaySound("ballhit.wav", winsound.SND_ASYNC)
        ball.dx*=-1
    if (ball.xcor()<-334 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+60 and ball.ycor()>paddle_a.ycor()-60):
        ball.setx(-334)
        winsound.PlaySound("ballhit.wav", winsound.SND_ASYNC)
        ball.dx*=-1
