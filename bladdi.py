import turtle as trtl

class OpticalSpiral:
    turtle_shapes = ["square", "circle", "triangle", "classic"]
    turtle_colors = ["purple", "red", "yellow", "blue"]
    turtle_dict = {
        "square": "purple",
        "circle": "red",
        "triangle": "yellow",
        "classic": "blue"
    }

    def __init__(self, shape, colors, x, y, direction):
        self.p = trtl.Turtle(shape=shape)
        self.p.speed(0)
        self.shape = shape
        self.colors = colors
        self.x = x
        self.y = y
        self.p.goto(x, y)
        self.direction = direction
        self.p.setheading(direction)

    def main(self):
        
