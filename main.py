from turtle import Turtle, Screen

from draw import relocate, center, draw_multiple_shapes, random_walk, draw_spirograph, draw_three_squares, hirst_generator

screen = Screen()
screen.colormode(255)

jack = Turtle()

# draw_three_squares(jack)
#
# draw_multiple_shapes(jack)
#
# random_walk(jack)
#
# draw_spirograph(jack)
#
hirst_generator(jack, 10, 10, 50)

screen.exitonclick()
