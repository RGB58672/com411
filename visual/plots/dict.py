import matplotlib.pyplot as plt
import random as rnd
def data():
  paths = {}
  print("What type of line would you like to use? (:, -- or -)")
  line = input()
  print("What type of colour would you like to use? (r, g or b)")
  colour = input()
  print("What type of style would you like to use? (o, s or ^)")
  style = input()
  paths['line'] = line
  paths['colour'] = colour
  paths['style'] = style
  return data
def generate ():
  print("How many lines would you like to display?")
  num_lines = int(input())
  for num_line in range(num_lines):
    values = data()
    x = rnd.sample(range(1, 10), 5)
    y = rnd.sample(range(1, 10), 5)
    format = f"{values['line']}{values['colour']}{values['style']}"

    plt.plot(x, y, format)
  plt.show()
def run():
  print("Running...")
  generate()
  print("Done!")
run()