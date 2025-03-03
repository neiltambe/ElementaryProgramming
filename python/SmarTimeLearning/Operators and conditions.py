#and

number = int(input("Enter a number: "))
if (number % 5 == 0 and number % 2 == 0):
  print(number, "is even and divisible by 5")
if (number % 3 == 0 and number % 4 == 0):
  print(number, " is divisble by 3 and 4")
else:
  print(number, "is not divisible by 2 and 5, or 3 and 4")

#or

number = int(input("Enter a number: "))
if (number % 5 == 0 or number % 2 == 0):
  print(number, "is even or divisible by 5")
if (number % 3 == 0 or number % 4 == 0):
  print(number, "is divisble by 3 or 4")
else: 
  print(number, "is not divisible by 2, 5, 3, or 4")