import math
import random

class Player:
  def __init__(self, letter):
    # letter is x or o
    self.letter = letter
  
  # we want all players to get their next move given a game
  def get_move(self, game):
    pass

class HumanPlayer(Player):
  def __init__(self, letter):
    super().__init__(letter)

  def get_move(self, game):
    valid_square = False
    val = None
    while not valid_square:
      square = input(self.letter + "'s turn. Input move (0-8):")
      # check if is a correct value casting into a int or is available on the the board
      try:
        val = int(square)
        if val not in game.available_moves():
          raise ValueError
        valid_square = True
      except ValueError:
        print("Invalid square. Don´t you be a newt!")
    return val

class RandomComputerPlayer(Player):
  def __init__(self, letter):
    super().__init__(letter)

  def get_move(self, game):
    square = random.choice(game.available_moves())
    return square

class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) #randomly chooese one
        else:
            #get the square based off the minmax algorithm
            square = self.minimax(game, self.letter)['position'] 
        return square

    def minimax(self, state, player):
        max_player = self.letter  #SmartComputerPlayer
        other_player = 'O' if player == 'X' else 'X'

        # first we want to check if the previous move is a winner
        if state.current_winner == other_player:
          # we should returno postition and score to keep track
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
        # no empty sqyares 
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize if player is the max player
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize if the player is the min player
        for possible_move in state.available_moves():
            # Step 1: make a move, try that spot
            state.make_move(possible_move, player)
            # step 2: recurse using minmax to simulate a game after that move
            sim_score = self.minimax(state, other_player) 
            # step 3: undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move
            # step 4: update the dictionaries if necessary
            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best