import turtle
from turtle import Turtle, Screen
import random

color_test = [
    (232, 251, 242), (197, 13, 32), (250, 237, 18),
    (40, 76, 189), (39, 216, 68), (229, 159, 46), (237, 226, 6), (27, 40, 156),
    (214, 75, 13), (16, 153, 16), (198, 15, 11), (243, 34, 165),
    (228, 18, 121), (74, 9, 31), (224, 141, 210), (11, 97, 61), (220, 160, 11),
    (18, 18, 43), (47, 214, 231), (11, 227, 239), (81, 73, 213), (237, 156, 221),
    (74, 212, 167), (78, 233, 203), (56, 233, 242), (4, 66, 41), (60, 15, 8)
]

turtle.colormode(255)
tim = Turtle()
tim.speed(0)
tim.penup()


def random_color():
    color_palette = random.choice(color_test)
    return color_palette


tim.hideturtle()
forward_distance = 50
angle = -90
tim.goto(-450, -375)
for _ in range(16):
    angle *= -1
    for _ in range(19):
        tim.dot(30, random_color())
        tim.forward(forward_distance)
    for _ in range(2):
        tim.left(angle)
        tim.forward(forward_distance)
