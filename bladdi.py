import turtle as trtl
import random


colors = ["white", "red", "pink", "purple", "blue", "yellow", "orange", "black", "green"]
p = trtl.Turtle()
p.speed(0)
p.hideturtle()
p.pensize(4)
center_lines = 4

def draw_lines(x, y):
    p.penup()
    x = 0
    y = 0
    p.goto(x, y)
    p.pendown()
    for lines in range(center_lines):
        color = random.choice(colors)
        p.color(color)
        p.forward(200)
        p.backward(200)
        p.right(60)

draw_lines(0, 0)

wn = trtl.Screen()
wn.mainloop()
