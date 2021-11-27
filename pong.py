#simple pong game
#coded by Amir Bekhit
#part1 ----- getting started

import turtle

win = turtle.Screen()
win.title("ATARI 800XL - CLASSIC PONG")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

#Score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball 
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.delta_x = 0.5 # moving by 0.5 pixels
ball.delta_y = 0.5

#Player Score - Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('grey')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: {}  ||  Player B : {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))

#Function 
def paddle_a_up ():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down ():
    y = paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up ():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down ():
    y = paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

#Keyboard triggiring
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "o")
win.onkeypress(paddle_b_down, "l")

#Main game loop
while True:
    win.update()  

    #Move the ball
    #ball.xcor and ycor --> means the current position of the ball which is 0, 0 
    ball.setx(ball.xcor() + ball.delta_x)
    ball.sety(ball.ycor() + ball.delta_y)

    #border checking - top and bottom
    if ball.ycor() >300:
        ball.sety(300)
        ball.delta_y *= -1
   
    if ball.ycor() < -300:
        ball.sety(-300)
        ball.delta_y *= -1
    
    #border checking - right and left
    if ball.xcor() > 390 :
        ball.goto(0,0)
        ball.delta_x *= -1
        score_a +=1
        pen.clear()
        pen.write("Player A: {}  ||  Player B : {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))


    if ball.xcor() < -390 :
        ball.goto(0,0)
        ball.delta_x *= -1    
        score_b +=1
        pen.clear()
        pen.write("Player A: {}  ||  Player B : {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))
        
    
    # Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 360) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40 ):
        ball.setx(340)
        ball.delta_x *= -1
   
    if (ball.xcor() < -340 and ball.xcor() > -360) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40 ):
        ball.setx(-340)
        ball.delta_x *= -1


    


