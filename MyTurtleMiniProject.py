import turtle

def plant_flowers(seeds):
    a = 0
    while a < 4:
        seeds.forward(100)
        seeds.right(90)
        a = a + 1
    

def my_flower():
    window = turtle.Screen()
    window.bgcolor("black")

    sinan = turtle.Turtle()
    sinan.shape("arrow")
    sinan.color("green")
    sinan.speed("fast")
    a = 0
    while a < 45:
        plant_flowers(sinan)
        sinan.right(10)
        a = a + 1
    sinan.forward(300)
    window.exitonclick()

my_flower()
