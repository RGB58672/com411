print("Do you prefer tea or coffee?")
preference = input()
if ((preference == "coffee")):
  print("Me too! Do you have sugar with your coffee?")
  sugar = input()
  print("And do you have milk with your coffee?")
  milk = input()
  if ((sugar == "yes") and (milk == "no")):
    print("Wow, you have your coffee the same way I do!")
  elif ((sugar == "no") and (milk == "no")):
    print("You must really like the bitter taste of coffee!")
  elif ((sugar == "yes") or (milk == "no")):
    print("That's almost the way I have my coffee")
  else:
    print("I'm sorry, please try again.")
elif ((preference == "tea")):
  print("I'm more of a coffee robot, but whatever floats your boat!")
else:
  print("I'm sorry, I didn't get that. Please try again.")