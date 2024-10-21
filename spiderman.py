import turtle as trtl
trtl.bgcolor("black")
p = trtl.Turtle()
p.speed(0)

def turn_left(degree):
    p.left(degree)

def turn_right(degree):
    p.right(degree)

def move(distance):
    p.forward(distance)

def circ(degree, extent):
    p.circle(degree, extent)

def up():
    p.penup()

def down():
    p.pendown()

def teleport(x,y):
    p.goto(x,y)

#oval face
def spider_man(color):
    turn_right(45)
    up()
    teleport(-75,-125)
    down()
    p.fillcolor(color)
    p.begin_fill()
    for i in range(2):
        circ(100,90)
        circ(200,90) 
    turn_left(135)
    p.end_fill()

    #web face
    #positioning
    up()
    teleport(0,0)
    down()

    #face straight lines
    p.pencolor("black")
    for i in range(12):
        p.setheading(-90)
        up()
        teleport(0,0)
        down()
        turn_left(30*(i-1))
        move(200)

    #web face curved lines
    up()
    teleport(-7.5,15)
    down()
    for i in range(6):
        p.setheading(-90)
        turn_right(60*(i-1))
        circ(15,60)

    up()
    teleport(37.5,75)
    down()
    for n in range(3):
        for i in range(12):
            p.setheading(-90)
            turn_right(30*(i-1))
            circ(75+25*n,30)
        if n==0:
            up()
            teleport(50,100)
            down()
        if n==1:
            up()
            teleport(62.5,125)
            down()

    #left_eye
    #outer eye
    p.pencolor("white")
    up()
    teleport(-100,-125)
    turn_left(90)
    move(250)
    turn_left(90)
    x,y = p.pos()
    turn_left(45)
    down()

    p.fillcolor("black")
    p.begin_fill()

    circ(75,120)
    circ(45,60)
    turn_left(45)
    up()
    teleport(x,y)
    turn_left(60)
    down()
    circ(160,-52)

    p.end_fill()


    #inner eye
    up()
    teleport(x+12.5,y-25)
    turn_left(125)
    down()

    p.fillcolor("white")
    p.begin_fill()

    circ(75*5/7,120)
    circ(45*5/7,60)
    turn_left(45)
    up()
    teleport(x+12.5,y-25)
    turn_left(60)
    down()
    circ(160*5/7,-51.25)

    p.end_fill()
    #ends here


    #right eye
    #outer eye
    up()
    teleport(88,125)
    down()
    turn_left(45)
    x2,y2 = p.pos()

    p.fillcolor("black")
    p.begin_fill()

    circ(75,-120)
    circ(45,-60)
    turn_left(45)

    up()
    teleport(x2,y2)
    turn_right(150)
    down()
    circ(160,52)
    p.end_fill()

    #inner eye
    up()
    teleport(x2-12.5,y2-25)
    down()

    p.fillcolor("white")
    p.begin_fill()

    turn_right(97.5)
    circ(45*5/7,-60)
    circ(75*5/7,-120)

    turn_right(45)
    up()
    teleport(x2-12.5,y2-25)
    turn_left(60)
    down()
    turn_right(142.25)
    circ(160*5/7,51.75)

    p.end_fill()
    p.hideturte()

wn = trtl.Screen()
wn.mainloop()
