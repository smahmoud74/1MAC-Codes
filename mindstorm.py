import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed("normal")

    count = 0
    while count <= 4:
        brad.forward(100)
        brad.right(90)
        count = count + 1

def draw_circle():
    
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

def draw_triangle():
    
    sinan = turtle.Turtle()
    sinan.shape("classic")
    sinan.color("black")
    sinan.speed(100)

    count = 0
    while count <= 3:
        sinan.forward(100)
        sinan.right(120)
        count = count + 1

    window.exitonclick()
    
draw_square()
draw_circle()
draw_triangle()
