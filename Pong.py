import turtle

win = turtle.Screen()
win.title("Pong by @Official_Uyi")
win.bgcolor("Black")
win.setup(width=800, height=600)
win.tracer(0)

#score
Score_a = 0
Score_b = 0

# paddle A
paddle_a =turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b =turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)



#Ball
Ball =turtle.Turtle()
Ball.speed(0)
Ball.shape("square")
Ball.color("white")
Ball.penup()
Ball.goto(0,0)
Ball.dx = 0.1
Ball.dy = -0.1


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0  Player B: 0", align="center", font=("Courier", 24, "normal"))




# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y += -20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y += -20
    paddle_b.sety(y)



#keyboard binding 
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Main Game Loop
while True:
    win.update()

    #move the ball
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    #Border checking
    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy *= -1

    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1

    if Ball.xcor() > 390:
        Ball.goto(0,0)
        Ball.dx*= -1
        Score_a += 1
        pen.clear()
        pen.write("PlayerA:{}  PlayerB: {}".format(Score_a, Score_b), align="center", font=("Courier", 24, "normal"))

    if Ball.xcor() < -390:
        Ball.goto(0,0)
        Ball.dx*= -1
        Score_b +=1
        pen.clear()
        pen.write("PlayerA:{}  PlayerB: {}".format(Score_a, Score_b), align="center", font=("Courier", 24, "normal"))




    # paddle and Bal Collisions
    if Ball.xcor() > 340 and Ball.xcor() < 350 and (Ball.ycor() < paddle_b.ycor() + 40 and Ball.ycor() > paddle_b.ycor() -40):
        Ball.setx(340)
        Ball.dx *= -1


    if Ball.xcor() < -340 and Ball.xcor() > -350 and (Ball.ycor() < paddle_a.ycor() + 40 and Ball.ycor() > paddle_a.ycor() -40):
        Ball.setx(-340)
        Ball.dx *= -1