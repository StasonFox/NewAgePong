import turtle
import winsound

# Background
screen = turtle.Screen()
screen.title("New Age Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Score
playerScore = 0
computerScore = 0

# Pen
pen = turtle.Turtle()
pen.color("Blue")
pen.speed(0)
pen.penup()
pen.goto(0, 260)
pen.hideturtle()
pen.write("Computer: 0 Player: 0", align="center", font=("Arial", 24, "normal"))

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("yellow")
ball.speed(0)
ball.goto(0, 0)
ball.penup()
ball.dx = 1
ball.dy = -1

# Left paddle
leftPad = turtle.Turtle()
leftPad.shape("square")
leftPad.shapesize(stretch_wid=5, stretch_len=1)
leftPad.color("blue")
leftPad.speed(0)
leftPad.goto(-350, 0)
leftPad.penup()

# Right paddle
rightPad = turtle.Turtle()
rightPad.shape("square")
rightPad.shapesize(stretch_wid=5, stretch_len=1)
rightPad.color("blue")
rightPad.speed(0)
rightPad.goto(350, 0)
rightPad.penup()

def rightPadUp():
    y = rightPad.ycor()
    y += 40
    rightPad.sety(y)

def rightPadDown():
    y = rightPad.ycor()
    y -= 40
    rightPad.sety(y)

def leftPadUp():
    y = leftPad.ycor()
    y += 10
    leftPad.sety(y)

def leftPadDown():
    y = leftPad.ycor()
    y -= 10
    leftPad.sety(y)

# Assign controls
screen.listen()
screen.onkeypress(rightPadUp, "Up")
screen.onkeypress(rightPadDown, "Down")

# Game loop
while True:
    screen.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border bounce
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        computerScore = computerScore + 1
        pen.clear()
        pen.write("Computer: {} Player: {}".format(computerScore, playerScore), align="center", font=("Arial", 24, "normal"))
        winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        playerScore = playerScore + 1
        pen.clear()
        pen.write("Computer: {} Player: {}".format(computerScore, playerScore), align="center", font=("Arial", 24, "normal"))
        winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)

    # Paddle bounce
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < rightPad.ycor() + 40 and ball.ycor() > rightPad.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < leftPad.ycor() + 40 and ball.ycor() > leftPad.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)

    # Computer movement
    if leftPad.ycor() < ball.ycor() and abs(leftPad.ycor() - ball.ycor()) > 10:
        leftPadUp()

    elif leftPad.ycor() > ball.ycor() and abs(leftPad.ycor() - ball.ycor()) > 10:
        leftPadDown()

    # Declare winner after 10 points
    if playerScore == 10:
        screen.bgcolor("black")
        pen.clear()
        pen.write("Player wins!", align="center", font=("Arial", 24, "normal"))
    elif computerScore == 10:
        screen.bgcolor("black")
        pen.clear()
        pen.write("Computer wins!", align="center", font=("Arial", 24, "normal"))