import random

game_outcome = [ "rock", "paper", "scissors" ]
def game_round(round_number):
  print()
  print("Round", round_number)
  my_choice = input("What do you want to play: ")
  computer_choice = random.randint(0, 2)
  print("Computer chose: ", game_outcome[computer_choice])
  if (game_outcome[computer_choice] == my_choice):
    print("It's a tie.")
  if (game_outcome[computer_choice] == game_outcome[0] and my_choice == game_outcome[1]):
    print("You win!! :)")
  if (game_outcome[computer_choice] == game_outcome[1] and my_choice == game_outcome[0]):
    print("Sorry.. you lose :(")
  if (game_outcome[computer_choice] == game_outcome[1] and my_choice == game_outcome[2]):
      print("You win!! :)")
  if (game_outcome[computer_choice] == game_outcome[2] and my_choice == game_outcome[1]):
      print("Sorry.. you lose :(")
  if (game_outcome[computer_choice] == game_outcome[0] and my_choice == game_outcome[2]):
      print("Sorry.. you lose :(")
  if (game_outcome[computer_choice] == game_outcome[2] and my_choice == game_outcome[0]):
      print("You win!! :)")

for i in range(5):
  game_round(i+1)