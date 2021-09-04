#Using random library to generate pseudo-random numbers
#Using multiple functions

import random

def play():
  """
  A simple Rock Paper Scissors game
  """

  rps = {'r': 'rock', 'p': 'paper', 's': 'scissors'}  #creats a dict to better print
  user = input("Whats your choice?\n r for rock, p for paper and s for scissors\n")
  
  if user not in rps:                                 #cheking for the right input
    return print('Stop being silly!')
  
  computer = random.choice(['r', 'p', 's'])           #generating computer choice

  if user == computer:
    print(f'You chose {rps[user]} and computer chose {rps[computer]}. So, it´s a tie.')
    return "It´s a tie"

  elif is_win(user,computer):                         #calling helpter function for test 
    print(f'You chose {rps[user]} and computer chose {rps[computer]}. So, you won.')
    return 'You won!'
  
  print(f'You chose {rps[user]} and computer chose {rps[computer]}. So, you lost.')
  return 'You lost'

def is_win(player, opponent):
  #helper function to check if the user have won
  if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponet == 'r'):
    return True
