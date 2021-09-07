import random
import string
import urllib.request, json 
from hangmanModule.hangman_visual import lives_visual_dict

# import a list of words from the web

with urllib.request.urlopen("https://www.randomlists.com/data/words.json") as url:
    download = json.loads(url.read().decode())
words = list(download.values())[0] # imported as list of lists. We only want the first item


# choose a word from the list
def get_valid_word(words):
  word = random.choice(words)   # randomly chooses something from the list
  while '-' in word or ' ' in word:
    word = random.choice(words)

  return word.upper()


# plays the game
def hangman():
  '''
  A simple hangman game.
  Lives equals the number of letters in the word plus one.
  '''
  print('\n|** A simple Hangman game **|\n')
  word = get_valid_word(words)  
  word_letters = set(word)       # letters in tahe word
  alphabet = set(string.ascii_uppercase)
  used_letters = set()           # what the user has guessed

  #number of lives based on the lenght of the word
  #visual based on the number of lives, but can´t be greater than 9
  lives = len(word_letters) + 1
  if lives > 9:
    visual = 9
  else:
    visual = lives


  #get user input
  while len(word_letters) > 0 and lives > 0:
    #informs used letters
    print('You have', lives, 'lives left and you have used these letters: ', ', '.join(used_letters))  

    #shows current state
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print(lives_visual_dict[visual]) 
    print('Keep guessing: ', ' '.join(word_list))

    user_guess = input('\nGuess a letter: ').upper()
    if user_guess in alphabet - used_letters:
      used_letters.add(user_guess)
      if user_guess in word_letters:
        word_letters.remove(user_guess)
      else:
        lives -= 1
        visual -= 1
        print("\nYou're wrong.\n")

    elif user_guess in used_letters:
      print('\nStop being silly, chose another letter!\n')
  
    else:
      print("\nThis is a dead parrot.\n")


  #while ends if the player have guessed or lost all lives
  if lives == 0:
    print(lives_visual_dict[100])
    print('Nobody expects the Spanish Inquisition! Our chief wepons are surprise and', word)
  else:
    print("That´s right, you witch!")
