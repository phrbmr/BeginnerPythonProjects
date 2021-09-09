# Main project

##importing projects



import madlibModule.simpleMadlib as ml
import rockPaperScissorsModule.rockPaperScissors as rps
import hangmanModule.hangman as hg
import ticTacToeModule.game as ttt
import guessModule.guessNumber as gn
import searchModule.search as sc
import mineModule.minesweeper as ms



menu = input('Choose your game:\n 1- Mad Libs\n 2- Guess the Number\n 3- Hangman\n 4- Rock Paper Scissors\n 5- Tic Tac Toe\n 6- Search\n 7- Minesweeper\n\n:>')
if menu == '1':
  ml.madlib()
elif menu == '2':
  gn.guess()
elif menu == '3':
  hg.hangman()
elif menu == '4':
  rps.play()
elif menu == '5':
  ttt.velha()
elif menu == '6':
  sc.search()
elif menu == '7':
  ms.menu()  
else:
  print ('Just a flesh wound!\n')
  print('''
                  _________
                 |         |
                 |         |
                 |         |
                 |         |
                 |         |
                 |         |
                 |         |
                 |         
                /                     
               /             ::::.
              /      )           ""::::
             |                         ":::"-..___
              \        ___.....____             `")
    -----------""----""            """----"""---'-------''')

  
