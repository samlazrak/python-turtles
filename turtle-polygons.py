import turtle
import random
from turtle import *

# Screen settings
window = turtle.Screen()
window.bgcolor("black")

# Turtle options
turtle.speed(0)
turtle.hideturtle()
turtle.pensize(2.5)

def draw_art(iterations, sides, length, right_distance, right_distance_divisor):

  for i in range(0, iterations):
    random_color()
    draw_polygon(turtle, sides, length, right_distance_divisor)
    turtle.right(right_distance)

def draw_polygon(turtle, sides, length, right_distance_divisor):
  for i in range(0, sides):
    random_color()
    turtle.forward(length)
    turtle.right(right_distance_divisor/sides)

def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  a = random.randint(0, 255)
  color = (r,g,b,a)
  turtle.color(color)

# iterations, sides, length, right right_distance, right_distance_divisor
length = 24
for i in range(0,100):
  print i
  length = length+1
  draw_art(38, 11, length, 20, 720)

