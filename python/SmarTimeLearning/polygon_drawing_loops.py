import turtle

t = turtle.Turtle()

polygon_sides = {"Triangle": 3,
                 "Square": 4,
                 "Pentagon": 5,
                 "Hexagon": 6,
                 "Heptagon": 7,
                 "Octagon": 8,
                 "Nonagon": 9,
                 "Decagon": 10,
                 "Undecagon": 11,
                 "Dodecagon": 12,
                 "Tridecagon": 13
                 }
polygon = "Tridecagon"
sides = polygon_sides[polygon]
angle_of_rotation = 360/polygon_sides[polygon]
polygon_sides = 0
length = 50 

while polygon_sides < sides :
    t.forward(length)
    t.left(angle_of_rotation)
    polygon_sides += 1
