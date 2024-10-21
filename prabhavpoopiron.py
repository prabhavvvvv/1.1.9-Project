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
    p.begin_fill
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

def draw_iron_man(x, y):
    #head
    head_colors = ["red", "green", "blue", "orange"]
    print(head_colors)

    new_color = "purple"
    head_colors.append(new_color)
    print(f"{new_color} has been added to the list. The current colors now are {head_colors}.")

    if len(head_colors) > 4:
        print("There are already enough colors in the list")
    else:
        head_colors.append("pink")

    while True:
        color_input = input("What color do you want Iron Man's head to be?: ").lower()
        if color_input in head_colors:
            print("Now drawing", color_input, "Iron Man...")
            break
        else:
            print("Invalid color, please try again")
    
    if color_input in head_colors:
        pass

    turn_right(45)
    up()
    teleport(x, y)
    down()
    p.fillcolor(color_input)
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

    # right eye
    up()
    teleport(-90, 20)
    p.pencolor("black")
    turn_right(150)
    p.color("black")
    down()
    p.circle(200, 45)
    p.fillcolor("cyan")
    p.begin_fill()
    turn_right(90)
    move(10)
    turn_right(80)
    move(30)
    turn_left(-45)
    move(30)
    turn_left(-60)
    move(5)
    p.end_fill()

    # left eye
    up()
    teleport(-90, 20)
    p.fillcolor("cyan")
    p.begin_fill()
    turn_left(190)
    down()
    move(10)
    turn_right(-30)
    move(35)
    turn_right(-60)
    move(24)
    p.end_fill()

    # mouth
    up()
    teleport(-65, -80)
    p.pencolor("black")
    p.pensize(7)
    turn_right(80)
    down()
    move(15)
    turn_right(-100)
    move(15)
    turn_right(60)
    p.setheading(0)
    move(60)
    turn_right(50)
    move(15)
    turn_right(-90)
    move(15)

    up()
    teleport(-90, 95)
    p.fillcolor("yellow")
    p.pencolor("yellow")
    p.pensize(5)
    p.begin_fill()
    down()
    turn_right(180)
    p.setheading(225)
    move(30)
    turn_right(-80)
    move(30)
    circ(-40, 30)
    circ(-40, -30)
    turn_left(-40)
    move(10)

def main():
    avengers_upper = ["Spiderman", "Iron Man"] 
    avengers__lower = ["spiderman", "iron man"]
    print("The available avengers that I can draw are", avengers_upper, "or", avengers__lower)
    print("Please type your input exactly how it is in the list")
    while True:
        avenger = input("What do you want me to draw?: ").lower()
         
        if avenger in avengers_upper or avenger in avengers__lower:
            if "spiderman" in avenger:
                print("Now drawing Spider-Man...")
                print("Fun fact: Spider-Man is the youngest superhero ever")
                draw_spiderman()
                break
            elif "iron man" in avenger:
                draw_iron_man(x = -75, y = -125)
                break
            else:
                print("Please enter a valid input")

if __name__ == "__main__":
    main()

wn = trtl.Screen()
wn.mainloop()
