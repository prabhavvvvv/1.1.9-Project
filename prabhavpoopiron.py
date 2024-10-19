import turtle as trtl
trtl.bgcolor("black")
p = trtl.Turtle()
p.pencolor("white")
p.speed(0)
r = "radius"

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

def web():
    p.pencolor("black")
    p.width(1)
    for angle in range(0, 360, 15):
        p.setheading(angle)
        p.up()
        p.goto(0, 0)
        p.down()
        p.forward(400)
        p.up()
        p.goto(0, 0)

    
def draw_spiderman():
    turn_right(45)
    up()
    teleport(-75,-125)
    down()
    p.fillcolor("red4")
    p.begin_fill()
    for i in range(2):
        circ(100, 90)
        circ(200, 90) 
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
    web()

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

def draw_iron_man(x, y, color):
    #head
    turn_right(45)
    up()
    teleport(x, y)
    down()
    p.fillcolor(color)
    p.begin_fill()
    for i in range(2):
        circ(100, 90)
        circ(200, 90) 
    turn_left(135)
    p.end_fill()

    up()
    teleport(-90, 95)
    p.fillcolor("yellow")
    p.begin_fill()
    p.pencolor("yellow")

    up()
    teleport(-90, 95)
    p.fillcolor("yellow")
    p.begin_fill()
    p.pencolor("yellow")
    p.right(30)
    r = 6
    circ(r, 20)
    p.setheading(45)
    down()
    p.pensize(5)
    move(60)
    turn_right(90)
    p.setheading(-80)
    move(80)
    turn_left(90)
    p.setheading(0)
    move(50)
    turn_right(-90)
    p.setheading(80)
    move(80)
    turn_right(90)
    p.setheading(-45)
    move(60)
    p.right(30)
    circ(50, 50)
    turn_right(90)
    circ(50, 50)
    p.setheading(0)
    turn_right(90)
    circ(-40, 50)
    turn_right(90)
    turn_right(-90)
    circ(60, 70)
    turn_right(-90)
    turn_right(90)
    turn_right(90)
    circ(60, 70)
    turn_left(-90)
    move(50)
    circ(-50, 50)

    # eyes
    up()
    teleport(-90, 50)
    p.pencolor("black")
    turn_right(150)
    p.fillcolor("white")
    p.begin_fill()

    move(40)
    turn_right(45)

    circ(-20, 90)

    move(40)
    turn_right(45)
    p.end_fill()

def main():
    faces_upper = ["Spiderman", "Iron Man"] 
    faces_lower = ["spiderman", "iron man"]
    print("The available faces that I can draw are", faces_upper, "or", faces_lower)
    print("Please type your input exactly how it is in the list")
    while True:
        face_input = input("What do you want to draw?: ")
        face_input = face_input.lower()
         
        if face_input in faces_upper or face_input in faces_lower:
            if "spiderman" in face_input:
                print("Now drawing Spiderman...")
                draw_spiderman()
                break
            elif "iron man" in face_input:
                print("Now drawing Iron Man...")
                draw_iron_man(x = -75, y = -125, color="red")
                break
            else:
                print("Please enter a valid input")

if __name__ == "__main__":
    main()

wn = trtl.Screen()
wn.mainloop()
