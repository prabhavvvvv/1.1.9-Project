import turtle as trtl
trtl.bgcolor("lightblue")
trtl.speed(0)

# code for spiderman face
def draw_spiderman_face():
    p = trtl.Turtle()
    p.penup()
    p.goto(0, -150)
    p.pendown()
    p.color("red")
    p.begin_fill()
    p.setheading(0)
    p.circle(150)
    p.end_fill()

# draws the eyes
def spiderman_eyes(x, y): # returns the x and y coordinates of the eye location
    #left eye
    p = trtl.Turtle()
    p.penup()
    p.goto(x, y)
    p.pendown()
    p.color("white")
    p.begin_fill()
    p.circle(30)
    p.end_fill()

    #right eye
    p.penup()
    p.goto(x + 70, y)
    p.pendown()
    p.begin_fill()
    p.circle(30)
    p.end_fill()

# code for batman face
def draw_batman_face():
    p = trtl.Turtle()
    p.penup()
    p.goto(-10, 0)
    p.pendown()
    p.color("black")
    p.begin_fill()
    p.setheading(0)
    p.circle(100)
    p.end_fill()

# draws batman's eyes
def batman_eyes(x, y): # returns the x and y coordinates of batman's eyes
   # left eye
   p = trtl.Turtle()
   p.penup()
   p.goto(x, y)
   p.pendown()
   p.color("white")
   p.begin_fill()
   p.circle(20)
   p.end_fill()

   #right eye
   p.penup()
   p.goto(x + 70, y)
   p.pendown()
   p.begin_fill()
   p.circle(20)
   p.end_fill()

# main function that includes the list of faces along with the user input
def main():
    faces_upper = ["Spiderman", "Batman"] 
    faces_lower = ["spiderman", "batman"]
    print("The available faces that I can draw are", faces_upper, "or", faces_lower)
    print("Please type your input exactly how it is in the list")

    face_input = input("What face do you want me to draw?: ")
    if face_input in faces_upper or face_input in faces_lower:
        if face_input == "Spiderman" or face_input == "spiderman":
            print("Now drawing Spiderman...")
            draw_spiderman_face()
            spiderman_eyes(-50, 50)
        elif face_input == "Batman" or face_input == "batman":
            print("Now drawing Batman...")
            draw_batman_face()
            batman_eyes(-50, 50)


if __name__ == "__main__":
    main()

