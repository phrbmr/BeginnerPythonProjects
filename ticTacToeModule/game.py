import math
import time
from ticTacToeModule.player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer

class TicTacToe():
  def __init__(self):
    self.board = self.make_board()
    self.current_winner = None

  @staticmethod
  def make_board():
    return [' ' for _ in range(9)]

  def print_board(self):
    for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
      print('| ' + ' | '.join(row) + ' |')

  @staticmethod
  def print_board_nums():
    # 0 | 1 | 2
    number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
    for row in number_board:
      print('| ' + ' | '.join(row) + ' |')

  def make_move(self, square, letter):
    if self.board[square] == ' ':
      self.board[square] = letter
      if self.winner(square, letter):
        self.current_winner = letter
      return True
    return False

  def winner(self, square, letter):
    # check the row
    row_ind = math.floor(square / 3)
    row = self.board[row_ind*3:(row_ind+1)*3]
    # print('row', row)
    if all([s == letter for s in row]):
      return True
    col_ind = square % 3
    column = [self.board[col_ind+i*3] for i in range(3)]
    # print('col', column)
    if all([s == letter for s in column]):
      return True
    if square % 2 == 0:
      diagonal1 = [self.board[i] for i in [0, 4, 8]]
      if all([s == letter for s in diagonal1]):
        return True
      diagonal2 = [self.board[i] for i in [2, 4, 6]]
      if all([s == letter for s in diagonal2]):
        return True
    return False

  def empty_squares(self):
    return ' ' in self.board

  def num_empty_squares(self):
    return self.board.count(' ')

  def available_moves(self):
    return [i for i, x in enumerate(self.board) if x == " "]


def play(game, x_player, o_player, print_game=True):
  if print_game:
    game.print_board_nums()

  letter = 'X'
  while game.empty_squares():
    if letter == 'O':
      square = o_player.get_move(game)
    else:
      square = x_player.get_move(game)
    if game.make_move(square, letter):

      if print_game:
        print(letter + ' makes a move to square {}'.format(square))
        game.print_board()
        print('')

      if game.current_winner:
        if print_game:
          print(letter + ' wins!')
        return letter  # ends the loop and exits the game
      letter = 'O' if letter == 'X' else 'X'  # switches player
    if print_game:
      time.sleep(.8)

  if print_game:
    print('It\'s a tie!')

def pcXpc():
  x_wins = 0
  o_wins = 0
  ties = 0
  for _ in range(1000):
    o_player = SmartComputerPlayer('O')
    x_player = HumanPlayer('X')
    result = play(t, x_player, o_player, print_game=false)



def velha():
  '''
  A simple Tic Tac Toe Game.
  3 modes: 
  - Against Random Computer
  - Agains MinMax 
  - Random X MinMAx
  '''
  print('\n|** A simple Tic Tac Toe game **|\n')
  #choose the opponent
  dif = input('Set difficulty: \n 1- Kights Who Say "Ni"\n 2- The Killer Rabbit of Caerbannog\n 3- Let them play\n    -> ')

  #test to see the user response
  if dif not in ('1','2', '3'):
    return print("Bugger off!")

  #against Random
  elif int(dif) == 1:
    o_player = RandomComputerPlayer('O')
    x_player = HumanPlayer('X')

  #against minmax
  elif int(dif) == 2:
    o_player = SmartComputerPlayer('O')
    x_player = HumanPlayer('X')

  #random against minmax
  elif int(dif) == 3:
    x_wins = 0
    o_wins = 0
    ties = 0
    iterations = int(input('Hou many times?\n    ->'))
    for _ in range(iterations):
      o_player = SmartComputerPlayer('O')
      x_player = RandomComputerPlayer('X')
      t = TicTacToe()
      result = play(t, x_player, o_player, print_game=False)
      if result == 'X':
        x_wins += 1
      elif result == 'O':
        o_wins += 1
      else:
        ties += 1
    print(f"After {iterations} iterations we have:\n {x_wins} 'X' wins\n {o_wins} 'O' wins\n {ties} ties")
    return True

  t = TicTacToe()
  play(t, x_player, o_player, print_game=True)

