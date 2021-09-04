import random
import string
import urllib.request, json 

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
  A simple handman game.
  '''
  word = get_valid_word(words)  
  word_letters = set(word)       # letters in tahe word
  alphabet = set(string.ascii_uppercase)
  used_letters = set()           # what the user has guessed

  user_guess = input('Guess a letter: ').upper()

  if user_guess in alphabet - used_letters:
    used_letters.remove(user_guess)
    if user_guess in word_letters:
      word_letters.remove(user_guess)

  elif user_guess in used_letters:
    print('Stop being silly, chose another letter!')
  
  else:
    print("This is a dead parrot.")
