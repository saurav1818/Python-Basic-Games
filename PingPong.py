import turtle


win = turtle.Screen()
win.title("Ping Pong")
win.bgcolor('black')
win.setup(width=800, height=600)
win.tracer(0) # it stops the window to update automatically we have to update manually

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.color('white')
paddle_a.shape('square')
paddle_a.penup()
paddle_a.setposition(-350,0)
paddle_a.shapesize(stretch_wid=5,stretch_len=1) # basic shape size is 20px for both len and wid

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.color('white')
paddle_b.shape('square')
paddle_b.penup()
paddle_b.goto(350,0)
paddle_b.shapesize(stretch_len=1,stretch_wid=5)

# Ball
ball = turtle.Turtle()
ball.color('white')
ball.shape('circle')
ball.penup()
ball.goto(0,0)
ball.dx = 0.5
ball.dy = -0.5

# Pen
pen = turtle.Turtle()
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: "+str(score_a) + " | Player B: "+str(score_b),align='center',font=('cursive',20,'normal'))

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard Binding
win.listen()
win.onkeypress(paddle_a_up,'w')
win.onkeypress(paddle_a_down,'s')
win.onkeypress(paddle_b_up,'Up')
win.onkeypress(paddle_b_down,'Down')


# Main game loop
while True:
    win.update()

    # Moving ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        score_a += 1
        pen.clear()
        pen.write("Player A: " + str(score_a) + " | Player B: " + str(score_b), align='center',
                  font=('cursive', 20, 'normal'))
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        score_b += 1
        pen.clear()
        pen.write("Player A: " + str(score_a) + " | Player B: " + str(score_b), align='center',
                  font=('cursive', 20, 'normal'))
        ball.dx *= -1

    # Paddle and Ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
