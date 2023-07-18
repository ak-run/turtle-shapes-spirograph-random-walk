import turtle as t
import random

# first creating our turtle Tim and its features
tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")
tim.speed("fastest")
screen = t.Screen()


# a function to create a random colour
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour


# a function to draw a spirograph
def draw_spirograph(n):
    n = min(n, 100)  # Limit n to a maximum of 100
    for _ in range(n):
        tim.color(random_color())
        tim.circle(100)
        angle = 360/n
        tim.left(angle)


# function to draw regular polygons
def draw_reg_polygons(num_sides):
    shape_angle = 360 / num_sides
    tim.color(random_color())
    tim.pensize(3)  # setting pen size wider for better visibility
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(shape_angle)


# function to draw a random walk, only straight angles
def random_walk(n):
    n = min(n, 100)  # Limit n to a maximum of 100
    # possible directions in a straight angle
    directions = [0, 90, 180, 270]
    tim.pensize(15)
    for _ in range(n):
        tim.color(random_color())
        tim.forward(30)
        tim.setheading(random.choice(directions))


draw_spirograph(50)

for shape_side_n in range(3, 11):
    draw_reg_polygons(shape_side_n)

random_walk(50)


screen.exitonclick()
