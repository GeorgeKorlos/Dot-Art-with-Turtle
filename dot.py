import random
import turtle
turtle.colormode(255)
timmy = turtle.Turtle()
 
color_list = [(203, 34, 66), (71, 116, 151), (228, 161, 193), (150, 184, 70), (151, 160, 164), (242, 235, 46), (37, 161, 80), (35, 31, 32), (137, 205, 187), 
              (240, 99, 54), (75, 65, 40), (33, 162, 165),]
 
timmy.penup()
position_y = -250
 
for _ in range(10):
    timmy.setposition(-250, position_y)
    position_y += 50
    for _ in range(10):
        timmy.dot(25, random.choice(color_list))
        timmy.penup()
        timmy.forward(50)
 
 
screen = turtle.Screen()
screen.exitonclick()