import turtle as trtl
p = trtl.Turtle()

p.speed(0)
trtl.bgcolor("black")
p.pensize(3)

turtle_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"] * 3

for i in range(20):
    p.color(turtle_colors[i])
    p.circle(200-10*i)
    

wn = trtl.Screen()
wn.mainloop()
