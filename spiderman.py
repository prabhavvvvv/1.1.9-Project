import turtle as trtl
trtl.bgcolor("black")
p = trtl.Turtle()
p.pencolor("white")
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


turn_right(45)
up()
teleport(-75,-125)
down()
p.fillcolor("red4")
p.begin_fill()
for i in range(2):
    circ(100,90)
    circ(200,90) 
turn_left(135)
p.end_fill()

#right_eye

#outer eye

up()
move(250)
turn_left(90)
move(25)
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





wn = trtl.Screen()
wn.mainloop()