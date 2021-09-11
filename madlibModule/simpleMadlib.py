# string concatenation
# 3 forms:
## print("some text and a " + var)
## print("some text and a {}".format(var))
## print(f"some text and a {var}")


def madlib ():
  """
  A simple madlib game
  """

  print('\n|** A simple Mad Lib **|\n')

  verb, sub, adjective = [], [], []


  print("Insert the words:")
  famous_person = input("Famous person: ")
  animal = input("Animal: ")
  animal2 = animal.upper()
  for i in range(3):
    verb.append(input(f"{i+1} Verb: "))
  for i in range(3):
    sub.append(input(f"{i+1} Substantive: "))
  for i in range(4):
    adjective.append(input(f"{i+1} Adjective: "))

  madlib = f"\nThis {animal} is no more! He has {verb[0]} to be! 'He's {adjective[0]} and gone to meet 'is {famous_person}! He's a {adjective[1]}! Bereft of life, 'e rests in {adjective[2]}! If you hadn't {verb[1]} 'im to the {sub[0]} he'd be {verb[2]} up the daisies! 'Is metabolic processes are now {adjective[3]}! 'E's off the {sub[1]}! He's kicked the {sub[2]}, he's shuffled off 'is mortal coil, run down the curtain and joined the bleedin' choir invisible!! THIS IS AN EX-{animal2}!!"

  print(madlib)

if __name__ == '__main__': # good practice
  madlib()