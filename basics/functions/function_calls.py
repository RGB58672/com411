def display_box(word):
  num_dashes = 4 + len(word)
  print("-" * num_dashes)
  print("| {} |".format(word))
  print("-" * num_dashes)
def display_lower_case(word):
  print(word.lower())
def display_upper_case(word):
  print(word.upper())
def display_mirrored(word):
  mirrored = ""
  for letter in reversed(word):
    mirrored += letter
  print("{} | {}".format(word,mirrored))
def display_repeat(word):
  print("How many times would you like the word to be repeated?")
  repeat = int(input())
  for repeat in range(repeats):
    if (repetition % 2 == 0):
      print(display_lower_case(word))
    else:
      print(display_upper_case(word))
def run():
  print("Please enter a word:")
  word = input()
  reponse = 0
  while (response != 6):
    print("What would you like to do with this word?")
    print("[1] Display in a box")
    print("[2] Display lower-case")
    print("[3] Display upper-case")
    print("[4] Display mirrored")
    print("[5] Display repeated")
    print("[6] Quit")
    repsonse = int(input())
    if (response == 1):
        display_box(word)
    elif (response == 2):
        display_lower_case(word)
    elif (response == 3):
        display_upper_case(word)
    elif (response == 4):
        display_mirrored(word)
    elif (response == 5):
        display_repeated(word)
    elif (response == 6):
        break
    else:
        print("Please try again.")
run()