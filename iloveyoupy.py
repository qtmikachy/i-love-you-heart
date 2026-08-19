import math
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=900, height=900)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.penup()
t.color("#ffb6c1")

def heart_x(angle, scale):
    return 16 * (math.sin(angle) ** 3) * scale

def heart_y(angle, scale):
    return (
        13 * math.cos(angle)
        - 5 * math.cos(2 * angle)
        - 2 * math.cos(3 * angle)
        - math.cos(4 * angle)
    ) * scale

for scale in range(11, 17):
    for i in range(120):
        angle = i * (math.pi * 2) / 120
        x = heart_x(angle, scale)
        y = heart_y(angle, scale)

        t.goto(x, y)
        t.write("kiss", align="center", font=("Arial", 8, "bold"))

def show_big_message():
    t.clear() 
    t.goto(0, -20)
    t.color("#ff4d6d") 
    t.write("I love you", align="center", font=("Arial", 36, "bold"))

screen.ontimer(show_big_message, 8000)

turtle.done()
# I hope you like it :D