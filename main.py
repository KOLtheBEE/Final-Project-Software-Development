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


#hangman
def get_valid_word(words):
  word = random.choice(words)
  while '-' in word or ' ' in word:
    word = random.choice(words)

  return word.upper()


def hangman():
  word = get_valid_word(words)
  word_letters = set(word)
  alphabet = set(string.ascii_uppercase)
  used_letters = set()
  lives = 6
  while len(word_letters) > 0 and lives > 0:
    print("Lives left: ", lives, "  Letters used: ", " ".join(used_letters))
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print("Current word: ", " ".join(word_list))
    user_letter = input("Guess a letter: ").upper()
    if user_letter in alphabet - used_letters:
      used_letters.add(user_letter)
      if user_letter in word_letters:
        word_letters.remove(user_letter)
      else:
        lives = lives - 1
        print("Letter is not in word.")
    elif user_letter in used_letters:
      print("Letter already used. Try again.")
    else:
      print("Invalid character. Try again.")
  if (lives == 0):
    print("You lost! The word was: ", word)
  else:
    print(f"You guessed the word: {word}!")


#tic tac toe


#print board
def print_board(board):
  for row in board:
    print(" | ".join(row))
    print("-" * 10)


# check winner
def check_winner(board):
  # Check rows
  for row in board:
    if row.count(row[0]) == len(row) and row[0] != '-':
      return row[0]

  # Check columns
  for col in range(len(board[0])):
    if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '-':
      return board[0][col]

  # Check diagonals
  if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
    return board[0][0]
  if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
    return board[0][2]

  return None


#full board
def is_board_full(board):
  return all("-" not in row for row in board)


#game logic
def tic_tac_toe():
  board = [['-' for _ in range(3)] for _ in range(3)]
  current_player = 'X'

  while True:
    print_board(board)
    row = int(input(f"Player {current_player}, choose row (1-3): ")) - 1
    col = int(input(f"Player {current_player}, choose column (1-3): ")) - 1

    if row < 0 or row > 2 or col < 0 or col > 2:
      print("Invalid move. Try again.")
      continue

    if board[row][col] == '-':
      board[row][col] = current_player
    else:
      print("That spot is already taken! Try again.")
      continue

    winner = check_winner(board)
    if winner:
      print_board(board)
      print(f"Player {winner} wins!")
      break
    elif is_board_full(board):
      print_board(board)
      print("It's a draw!")
      break

    current_player = 'O' if current_player == 'X' else 'X'


#menu
def menu():
  print("====== Main menu ======\n")
  print("1. Rock paper scissors\n")
  print("2. Hangman\n")
  print("3. Tic tac toe\n")
  print("4. Exit\n")


#main
menu()
choice = input("Select a game (1-3): ")
while (choice != 4):
  if choice == "1":
    rps()
    print("\n")
    menu()
    choice = input("Select a game (1-3): ")
  elif choice == "2":
    hangman()
    print("\n")
    menu()
    choice = input("Select a game (1-3): ")
  elif choice == "3":
    tic_tac_toe()
    print("\n")
    menu()
    choice = input("Select a game (1-3): ")
  else:
    choice = 4
print("Exiting...")
