import turtle
rainbow_color = ("red", "orange", "yellow", "green",
                 "cyan", "blue", "purple")
turtle.pensize(50)
x, y = 0, 0
color_index = 0
for color_index in range(7):
    turtle.pencolor(rainbow_color[color_index])
    turtle.penup()
    turtle.goto(x - 100, y - 100)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(200)
        turtle.left(90)
turtle.done()