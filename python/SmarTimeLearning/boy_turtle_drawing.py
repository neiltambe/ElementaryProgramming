#boy_turtle_drawing.py

import turtle

t = turtle.Turtle()

radius = int(input("Enter radius of my Circle"))
length = int(input("Enter length of my Rectangle"))
width = int(input("Enter width of my Rectangle"))

t.circle(radius)

t.goto(30,3)

t.backward(length)
t.right(90)

t.forward(width)
t.left(90)

t.forward(length)
t.left(90)

t.forward(width)
t.right(90)

t.right(90)
t.forward(width/2)

t.left(120)
t.forward(60)

t.backward(60)
t.left(60)

t.forward(width/2)
t.left(90)

t.forward(length)
t.left(90)

t.forward(width/2)
t.right(120)

t.forward(60)
t.backward(60)

t.left(120)
t.forward(width/2)

t.left(90)
t.forward(4)

t.right(90)
t.forward(70)

t.backward(70)
t.left(90)

t.forward(length-8)
t.right(90)

t.forward(70)
t.backward(70)

t.right(90)
t.forward(4)

t.left(90)







