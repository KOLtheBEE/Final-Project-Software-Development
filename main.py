import random
import string

from words import words


#rock paper scissors
def rps():
  print("What is your choice?")
  user = input("'r' is for rock, 'p' is for paper, 's' is for scissors\n")
  computer = random.choice(['r', 'p', 's'])
  if user == computer:
    print(f"Player: {user}\tComputer: {computer}.\nIt's a tie!\n")
  elif is_win_rps(user, computer):
    print(f"Player: {user}\tComputer: {computer}.\nYou won!\n")
  else:
    print(f"Player: {user}\tComputer: {computer}.\nYou lost!\n")
  return 0


def is_win_rps(player, opponent):
  if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
  or (player == 'p' and opponent == 'r'):
    return True
