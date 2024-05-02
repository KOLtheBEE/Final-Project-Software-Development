import unittest
from io import StringIO
from unittest.mock import patch

from main import *


class TestMain(unittest.TestCase):

  #First Test
  @patch('builtins.input', side_effect=['r'])
  @patch('random.choice', return_value='r')
  @patch('sys.stdout', new_callable=StringIO)
  def test_rps_equal(self, mock_stdout, mock_random_choice, mock_input):
    expected_output = (
        "What is your choice?\nPlayer: r\tComputer: r.\nIt's a tie!\n\n")

    rps()

    actual_output = mock_stdout.getvalue()

    #print(actual_output)

    self.assertEqual(actual_output, expected_output)

  # Second Test
  @patch('builtins.input', side_effect=['r'])
  @patch('random.choice', return_value='s')
  @patch('sys.stdout', new_callable=StringIO)
  def test_rps_player_wins(self, mock_stdout, mock_random_choice, mock_input):
    expected_output = (
        "What is your choice?\nPlayer: r\tComputer: s.\nYou won!\n\n")

    rps()

    actual_output = mock_stdout.getvalue()

    #print(actual_output)

    self.assertEqual(actual_output, expected_output)

  # Third Test
  @patch('builtins.input', side_effect=['r'])
  @patch('random.choice', return_value='p')
  @patch('sys.stdout', new_callable=StringIO)
  def test_rps_computer_wins(self, mock_stdout, mock_random_choice,
                             mock_input):
    expected_output = (
        "What is your choice?\nPlayer: r\tComputer: p.\nYou lost!\n\n")

    rps()

    actual_output = mock_stdout.getvalue()

    #print(actual_output)

    self.assertEqual(actual_output, expected_output)


  
  # Fourth test
  @patch('sys.stdout', new_callable=StringIO)
  def test_is_wins_rps(self, mock_stdout):

    player_choice = 'r'
    opponent_choice = 's'
    result = is_win_rps(player_choice, opponent_choice)

    self.assertTrue(result)

    player_choice = 's'
    opponent_choice = 'p'
    result = is_win_rps(player_choice, opponent_choice)

    self.assertTrue(result)

    player_choice = 'p'
    opponent_choice = 'r'
    result = is_win_rps(player_choice, opponent_choice)
  
    self.assertTrue(result)



  # Fifth Test
  '''
  @patch('sys.stdout', new_callable=StringIO)
  @patch('builtins.input', side_effect=['A'])
  def test_hangman_correct_letter(self, mock_input, mock_stdout):
      # Set the word and used letters for testing
    word_letters = {'F', 'A', 'N'}  # Mock the word letters set
    used_letters = {'A'}  # Mock the used letters set

    # Call the function with mocked sets
    with patch('__main__.set', side_effect=[word_letters, used_letters]):
        hangman()

    # Capture the output printed by the function
    actual_output = mock_stdout.getvalue().strip()

    #print(actual_output)
    
    # Define the expected output
    expected_output = "Lives left: 6  Letters used: A  Current word: - A -\nGuess a" \
    "letter: "

    
  
    # Check if the actual output matches the expected output
    self.assertEqual(actual_output, expected_output)
  '''

  # Sixth Test
  '''
  #print("Letter is not in word.")
  @patch('builtins.input', side_effect=['r'])
  @patch('random.choice', return_value='r')
  @patch('sys.stdout', new_callable=StringIO)
  def test_hangman_incorrect_letter(self, mock_stdout, mock_random_choice, mock_input):
    expected_output = (
        "Letter is not in word.\n\n")

    hangman()

    actual_output = mock_stdout.getvalue()

    print(actual_output)

    self.assertEqual(actual_output, expected_output)
  '''

  #
  def test_print_board(self):
    # Redirect stdout to capture printed output
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        board = [['X', '-', 'O'], ['-', 'X', 'O'], ['O', '-', 'X']]
        print_board(board)
        expected_output = (
          "X | - | O\n"
          "----------\n"
          "- | X | O\n"
          "----------\n"
          "O | - | X\n"
          "----------\n"
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)

  #
  def test_check_winner(self):
    # Test for horizontal win
    board_horizontal_win = [['X', 'X', 'X'], ['-', '-', '-'], ['-', '-', '-']]
    self.assertEqual(check_winner(board_horizontal_win), 'X')

    # Test for vertical win
    board_vertical_win = [['O', '-', '-'], ['O', '-', '-'], ['O', '-', '-']]
    self.assertEqual(check_winner(board_vertical_win), 'O')

    # Test for diagonal win
    board_diagonal_win = [['X', '-', '-'], ['-', 'X', '-'], ['-', '-', 'X']]
    self.assertEqual(check_winner(board_diagonal_win), 'X')


  def test_is_board_full(self):
    # Test for full board
    full_board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']]
    self.assertTrue(is_board_full(full_board))

    # Test for non-full board
    non_full_board = [['X', '-', 'X'], ['-', 'O', '-'], ['O', '-', 'O']]
    self.assertFalse(is_board_full(non_full_board))

  # Proper command output
if __name__ == '__main__':
  unittest.main()
