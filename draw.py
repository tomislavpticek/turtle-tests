import random
import colorgram


def draw_square(turtle_var):
    for var in range(0, 4):
        turtle_var.forward(100)
        turtle_var.right(90)


def draw_dashed_line_square(turtle_var):
    for var in range(0, 4):
        draw_dashed_line(turtle_var)
        turtle_var.right(90)


def draw_dashed_line(turtle_var):
    for var in range(0, 5):
        turtle_var.pencolor(random_color())
        turtle_var.forward(10)
        turtle_var.penup()
        turtle_var.forward(10)
        turtle_var.pendown()


def draw_dotted_square(turtle_var):
    for var in range(0, 4):
        for var2 in range(0, 10):
            turtle_var.pencolor(random_color())
            turtle_var.dot(5)
            turtle_var.penup()
            turtle_var.forward(10)
            turtle_var.pendown()
        turtle_var.right(90)


def draw_three_squares(turle_var):
    center(turle_var)
    draw_square(turle_var)
    relocate(turle_var)
    draw_dashed_line_square(turle_var)
    relocate(turle_var)
    draw_dotted_square(turle_var)


def relocate(turtle_var):
    turtle_var.penup()
    turtle_var.forward(200)
    turtle_var.pendown()


def center(turtle_var):
    turtle_var.penup()
    turtle_var.left(180)
    turtle_var.forward(250)
    turtle_var.right(90)
    turtle_var.forward(50)
    turtle_var.right(90)
    turtle_var.pendown()


def random_color():
    return (random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255))


def draw_multiple_shapes(turtle_var):
    for var in range(3, 10):
        turtle_var.pencolor(random_color())
        for side in range(var):
            turtle_var.forward(100)
            turtle_var.right(360 / var)


def random_walk(turtle_var):
    turtle_var.pensize(5)
    turtle_var.speed(0)
    for var in range(0, 1000):
        direction = random.randint(0, 1)
        degree = random.choice([0, 90, 180, 270, 360])
        if direction == 0:
            turtle_var.right(degree)
        else:
            turtle_var.left(degree)
        turtle_var.pencolor(random_color())
        turtle_var.forward(5)


def draw_spirograph(turtle_var):
    turtle_var.speed(0)
    step = 3
    for var in range(0, 360, step):
        turtle_var.left(step)
        turtle_var.pencolor(random_color())
        turtle_var.circle(100)


def relocate_v2(turtle_var, x, y):
    turtle_var.penup()
    turtle_var.setx(x)
    turtle_var.sety(y)
    turtle_var.pendown()
    return turtle_var


def hirst_generator(turtle_var, dot_size, space_between_dots, grid_size):
    colors = colorgram.extract('hirst.jpg', 71)
    inital_relocate_x = -(grid_size * space_between_dots * 2) / 2
    inital_relocate_y = -(grid_size * space_between_dots * 2) / 2
    dot_space = space_between_dots * 2
    tmp_turtle = relocate_v2(turtle_var, inital_relocate_x, inital_relocate_y)
    tmp_turtle.hideturtle()
    tmp_turtle.speed(0)
    for y in range(grid_size):

        for x in range(grid_size):
            tmp_turtle.pencolor(random.choice(colors).rgb)
            tmp_turtle.dot(dot_size)
            tmp_turtle.penup()
            tmp_turtle.forward(dot_space)
            tmp_turtle.pendown()

        tmp_turtle = relocate_v2(turtle_var, inital_relocate_x, (tmp_turtle.ycor() + dot_space))
