#https://colab.research.google.com/drive/1psr2feIwWd63L_JHCAS6NSI7s23kFoAJ#scrollTo=Ib8ACt1guC5t&uniqifier=1
!pip install ColabTurtlePlus==1.5
from math import pi
from ColabTurtlePlus.Turtle import *
initializeTurtle()

n = int(input("Enter number of sides"))
sum_of_interior_angles = (n-2)*180
angle = int(sum_of_interior_angles/n)
i = 1
while i <= n:
  forward(50)
  left(180-angle)
  i += 1