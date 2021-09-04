# string concatenation
# 3 forms:
## print("some text and a " + var)
## print("some text and a {}".format(var))
## print(f"some text and a {var}")


def madlib ():
  """
  A simple madlib game
  """
  famous_person = input("Famous person:")
  verb = input("Verb: ")
  adj = input("Adjective: ")

  madlib = f"He´s not the {famous_person}, he´s a {verb} {adj} boy!"

  print(madlib)