import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle named "roblox_turtle"
roblox_turtle = turtle.Turtle()
roblox_turtle.speed("fastest")  # Set the drawing speed

# Draw the red square
roblox_turtle.color("red")
roblox_turtle.begin_fill()
for _ in range(4):
    roblox_turtle.forward(100)
    roblox_turtle.left(90)
roblox_turtle.end_fill()

# Hide the turtle cursor
roblox_turtle.hideturtle()

# Keep the window open until manually closed
turtle.done()
5
