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
