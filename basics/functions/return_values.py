def sum_weights(beep_weight, bop_weight):
  total_weight = beep_weight + bop_weight
  return total_weight
def calc_average_weight(beep_weight, bop_weight):
  average_weight = (beep_weight + bop_weight) / 2
  return average_weight
def run():
  print("What is Beep's weight?")
  beep_weight = float(input())
  print("What is Bop's weight?")
  bop_weight = float(input())
  print("Would you like to know their average or total weight?")
  action = input()
  if (action == "total weight"):
    answer = sum_weights(beep_weight, bop_weight)
    print("Beep and Bop's total weight is {:.2f}".format(answer))
  elif (action == "average weight"):
    answer = calc_average_weight(beep_weight, bop_weight)
    print("Beep and Bop's average weight is {:.2f}".format(answer))
  else:
    print("Sorry, I didn't get that. Please try again.")

run()