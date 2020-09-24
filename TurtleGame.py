import turtle

import random

win = turtle.Screen()
win.title('Turtle Race')
win.bgcolor('black')
win.setup(width=800,height=600)

t1 = turtle.Turtle()
t1.color('white')
t1.shape('turtle')
t1.penup()
t1.setposition(0,-280)
t1.setheading(90)
t1.pendown()

t2 = turtle.Turtle()
t2.color('red')
t2.shape('turtle')
t2.penup()
t2.setposition(80,-280)
t2.setheading(90)
t2.pendown()

t3 = turtle.Turtle()
t3.color('green')
t3.shape('turtle')
t3.penup()
t3.setposition(160,-280)
t3.setheading(90)
t3.pendown()

t4 = turtle.Turtle()
t4.color('yellow')
t4.shape('turtle')
t4.penup()
t4.setposition(-80,-280)
t4.setheading(90)
t4.pendown()

t5 = turtle.Turtle()
t5.color('purple')
t5.shape('turtle')
t5.penup()
t5.setposition(-160,-280)
t5.setheading(90)
t5.pendown()

pen = turtle.Turtle()
pen.setposition(320,250)
pen.color('white')
pen.hideturtle()
pen.write('Winner:\n', align='center', font='Courier')

rand1 = random.randrange(1,31,3)
rand2 = random.randrange(1,31,3)
rand3 = random.randrange(1,31,3)
rand4 = random.randrange(1,31,3)
rand5 = random.randrange(1,31,3)

file = open('C:/Users/HP/Desktop/Demo.txt','a')

for i in range(100):
    t1.forward(rand1)
    if t1.ycor() > 280:
        pen.write('White Wins', font='Courier')
        file.write('White Wins')
        break
    t2.forward(rand2)
    if t2.ycor() > 280:
        pen.write('Red Wins',font='Courier')
        file.write('Red Wins')
        break

    t3.forward(rand3)
    if t3.ycor() > 280:
        pen.write('Green Wins',font='Courier')
        file.write('Green Wins')
        break

    t4.forward(rand4)
    if t4.ycor() > 280:
        pen.write('Yellow Wins',font='Courier')
        file.write('Yellow Wins')
        break

    t5.forward(rand5)
    if t5.ycor() > 280:
        pen.write('Purple Wins',font='Courier')
        file.write('Purple Wins')
        break

file.close()



turtle.mainloop()

