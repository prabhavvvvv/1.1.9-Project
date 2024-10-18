import turtle as trtl
p = trtl.Turtle()

def draw_spiderman():
    p.circle(100,90)
    
def draw_batman():
    print("batman")

while True:
    user_input = input("What do you want to draw?")
    user_input = user_input.lower()
    user_input = user_input.split()
    if "spiderman" in user_input:
        draw_spiderman()
        break
    elif "batman" in user_input:
        draw_batman()
        break




wn = trtl.Screen()
wn.mainloop()
