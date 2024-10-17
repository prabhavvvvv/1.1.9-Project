import turtle as trtl
trtl.bgcolor("lightblue")
trtl.speed(0)

# code for spiderman face
def draw_spiderman_face():
    p = trtl.Turtle()
    p.penup()
    p.goto(-10, 0)
    p.pendown()
    p.color("red")
    p.begin_fill()
    p.setheading(0)
    p.end_fill()

def spiderman_eyes(x, y):
    p = trtl.Turtle()
    x = 200
    y = 200
    p.penup()
    p.goto(x, y)

# code for batman face
def draw_batman_face():
    p = trtl.Turtle()
    p.penup()


def main():
    faces_upper = ["Spiderman", "Batman"]
    faces_lower = ["spiderman", "batman"]
    print("The available faces that I can draw are", faces_upper, "or", faces_lower)
    print("Please type your input exactly how it is in the list")


    face_input = input("What face do you want me to draw? :")
    if face_input in faces_upper or face_input in faces_lower:
        if face_input == "Spiderman" or face_input == "spiderman":
            draw_spiderman_face()
        elif face_input == "Batman" or face_input == "batman":
            draw_batman_face

if __name__ == "__main__":
    main()
