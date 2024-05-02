import unittest
from io import StringIO
from unittest.mock import patch

from main import rps


class TestMain(unittest.TestCase):

  @patch('builtins.input', side_effect=['r'])
  @patch('random.choice', return_value='r')
  @patch('sys.stdout', new_callable=StringIO)

  #First Test
  def test_rps_equal(self, mock_stdout, mock_random_choice, mock_input):
    expected_output = ("What is your choice?\nPlayer: r\tComputer: r.\nIt's a tie!\n\n")

    rps()

    actual_output = mock_stdout.getvalue()

    print(actual_output)

    self.assertEqual(actual_output, expected_output)

  

  @patch('builtins.input', side_effect=['r'])
  @patch('random.choice', return_value='s')
  @patch('sys.stdout', new_callable=StringIO)

  # Second Test
  def test_rps_player_wins(self, mock_stdout, mock_random_choice, mock_input):
    expected_output = ("What is your choice?\nPlayer: r\tComputer: s.\nYou won!\n\n")

    rps()

    actual_output = mock_stdout.getvalue()

    print(actual_output)

    self.assertEqual(actual_output, expected_output)

  

  @patch('builtins.input', side_effect=['r'])
  @patch('random.choice', return_value='p')
  @patch('sys.stdout', new_callable=StringIO)
  
  # Third Test
  def test_rps_computer_wins(self, mock_stdout, mock_random_choice, mock_input):
    expected_output = ("What is your choice?\nPlayer: r\tComputer: p.\nYou lost!\n\n")
  
    rps()
  
    actual_output = mock_stdout.getvalue()
  
    print(actual_output)
  
    self.assertEqual(actual_output, expected_output)



    

  # Proper command output
if __name__ == '__main__':
  unittest.main()
