!pip install ColabTurtle
from ColabTurtle.Turtle import *

initializeTurtle()

list_drawings = ["boy", "girl", "square", "rectangle", "circle"]
turtle_speed = speed

choice = input("What do you want to draw?")

def circle(radius, type:str="full"):
    speed(13)
    degrees = 360
    if type == "semi":
      degrees = 180
    for _ in range(degrees):  
        forward(2 * 3.1416 * radius / 360) 
        right(1)  

def draw_boy():
    # Body
    forward(100)
    left(90)
    forward(50)
    left(90)
    forward(100)
    left(90)
    forward(50)
    # Body

    # Head
    penup()
    left(90)
    forward(100)
    left(90)
    forward(25)
    pendown()
    circle(40)
    # Head

    # Arms
    forward(25)
    left(90)
    forward(25)
    right(120)
    forward(60)
    penup()
    backward(60)
    right(60)
    forward(25)
    right(90)
    forward(50)
    right(90)
    forward(25)
    left(120)
    pendown()
    forward(60)
    backward(60)
    # Arms
  
    # Legs
    right(120)
    forward(75)
    right(90)
    forward(13)
    left(90)
    forward(90)
    backward(90)
    right(90)
    forward(24)
    left(90)
    forward(90)
    backward(90)
    # Legs 

def draw_girl(): 
  # Body
  left(150)
  forward(150)
  left(120)
  forward(150)
  left(120)
  forward(150)
  # Body

  # Head  
  left(60)
  circle(50)
  # Head

  # Arms
  left(60)
  penup()
  forward(50)
  right(100)
  pendown()
  forward(60)
  penup()
  backward(60)
  right(80)
  forward(50)
  right(120)
  forward(50)
  left(100)
  pendown()
  forward(60)
  # Arms

  # Legs
  penup()
  backward(60)
  right(100)
  forward(100)
  right(120)
  forward(38)
  left(90)
  pendown()
  forward(90)
  penup()
  backward(90)
  right(90)
  forward(74)
  left(90)
  pendown()
  forward(90)
  penup()
  backward(90)
  # Legs

def draw_square(length = 100):
  for i in range(4):
    left(90)
    forward(length)

def draw_rectangle():
  for i in range(2):
    left(90)
    forward(100)
    left(90)
    forward(50)

def draw_funny_face():
  draw_square(10)
  penup()
  left(90)
  forward(150)
  pendown()
  draw_square(10)
  penup()
  right(180)
  forward(150)
  right(90)
  forward(100)
  pendown()
  circle(75, "semi")

    
if choice == "boy" :
  draw_boy()
elif choice == "girl" :
  draw_girl()
elif choice == "square" :
  draw_square()
elif choice == "rectangle" :
  draw_rectangle()
elif choice == "circle" :
  circle(50)
else:
  draw_funny_face()