import turtle
amy = turtle.Turtle()
amy.color("cyan")
amy.speed(0)
def draw_square():
    for side in range(4):
        amy.forward(100)
        amy.right(90)
        for side in range(4):
            amy.forward(50)
            amy.right(90)
draw_square()

def new_function():
    for suqre in range(30):
        draw_square()
        amy.ponup()
        amy.forward(20)
        amy.left(45)
        amy.pendown()
new_function()