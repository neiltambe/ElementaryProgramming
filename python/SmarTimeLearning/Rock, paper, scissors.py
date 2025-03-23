!pip install colabTurtle
import turtle 
from ColabTurtle.Turtle import *
initializeTurtle()
turtle = Turtle()
list_drawings = ["boy", "girl", "square", "rectangle", "circle"]

def boy_function():
#body
  forward(100)
  left(90)
  forward(50)
  left(90)
  forward(100)
  left(90)
  forward(50)
#body
  penup()
  left(90)
  forward(100)
  left(90)
  forward(25)
  circle(100)


boy_function()