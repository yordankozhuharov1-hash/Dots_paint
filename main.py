import turtle as t  
import random

t.speed("fastest")
# 1. Hide the turtle cursor and lift the pen so it doesn't draw lines
t.hideturtle()
t.penup()

color_list = [(203, 161, 90), (59, 89, 128), (141, 91, 44), (136, 173, 197), (135, 27, 50), (220, 207, 113), (153, 52, 84), (35, 42, 67), (169, 157, 43), (45, 55, 103), (132, 186, 144), (80, 18, 40), (188, 140, 162), (183, 93, 106), (57, 38, 28), (89, 122, 176), (89, 154, 96), (80, 151, 161), (63, 127, 113), (194, 88, 71), (78, 73, 43), (161, 201, 217), (220, 175, 189), (45, 73, 77), (170, 206, 166), (222, 181, 167)]
t.colormode(255)

t.setheading(225)
t.forward(300)
t.setheading(0)

number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    t.dot(20, random.choice(color_list))
    t.forward(50)

    if dot_count % 10 == 0:
        # Removed the duplicate t.dot() here to prevent double dots at the ends of rows
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

screen = t.Screen()
screen.exitonclick()
