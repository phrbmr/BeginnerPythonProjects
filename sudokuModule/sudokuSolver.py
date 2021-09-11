from pprint import pprint
from sudokuModule.board import example_board

####################
# Helper functions #
####################

def find_next_empty(puzzle):
  #finds the next row, col non the puzzle that´s not filled (-1)
  #indices are 0-8
  #return row, col tuple, or None, None
  for r in range(9):
    for c in range(9):
      if puzzle[r][c] == -1: 
        return r, c   #empty space index
  
  return None, None #if no spaces in the puzzle are empty

def is_valid(puzzle, guess, row, col):
  # figures out whether the guess ate the row/col is valid
  # returns True if valid, False otherwise
  
  #check the rows
  row_vals = puzzle[row]
  if guess in row_vals:
    return False
  
  #create a column list and check
  col_vals = [puzzle[i][col] for i in range(9)]
  if guess in col_vals:
    return False
  
  #get where the 3x3 square starts and iterate over the 3 values in the row/column
  row_start = (row // 3) * 3 #find wich set of rows ( 1 // 3 = 0 , 5 // 3 = 1 , ...)
  col_start = (col // 3) * 3 

  for r in range(row_start, row_start + 3):
    for c in range(col_start, col_start + 3):
      if puzzle[r][c] == guess:
        return False
  
  # if the guess was not found, then it´s a valid guess
  return True

###################
# Solver function #
###################

def solve_sudoku(puzzle):
  ''''
  - A simples sudoku solver 
  - Solve sudoku using backtraking
  - The puzzle is a list of lists, where the inner list is a list
  - Return whether a solution exists
  - If exists, mutates the puzzle to be the solution
  '''

  #step 1: choose somwhere to make a guess
  row, col = find_next_empty(puzzle)

  #step 1.1: if there´s nowhere left, the we´re done
  if row is None:
    return True
  
  #step 2: if there is a place to put a guess, then make a guess between 1 and 9
  for guess in range(1, 10):      # range(1 ,10) is 1..9
    #Step 3: check if is a valid guess
    if is_valid(puzzle, guess, row, col):
      #step 3.1: if valid, place that guess on the puzzle
      puzzle[row][col] = guess
      #step 4: recursively call our function
      if solve_sudoku(puzzle):
        return True
    
    #step 5: if not valid OR if guess did not solved the game, go to the next guess

    puzzle[row][col] = -1 #reset guess

  #step 6: if none of the numbers work, there´s no possible solution
  return False

def run():
  print(solve_sudoku(example_board))
  pprint(example_board)

if __name__ == '__main__': # good practice
  sudoku()