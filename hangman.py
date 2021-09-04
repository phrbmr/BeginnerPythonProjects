import random
import string
import urllib.request, json 

# import a list of words from the web
with urllib.request.urlopen("https://www.randomlists.com/data/words.json") as url:
    words = json.loads(url.read().decode())

def get_valid_word(words):
  word = random.choice(words)   # randomly chooses something from the list

  while '-' in word or ' ' in word:
    word = random.choice(words)
  
  return word.upper()

def hangman():
  word = get_valid_word(words)  
  word_letter = set(word)       # letters in the word
  alphabet = set(string.ascii_uppercase)
  used_letters = set()          # what the user has guessed

  user_letter = input('Guess a letter: ').upper()

  if user_letter in alphabet - used_letters:
    word_letter.remove(user_letter)

  elif user_letter in used_letters:
    print('Stop being silly, chose a not used letter.')
  
  else:
    print("This is a dead parrot.")

