print("Where should I look?")
where = input()
if (where == "in the bedroom"):
  print("Where in the bedroom should I look?")
  look = input()
  if (look == "under the bed"):
    print("Found some shoes but not a battery")
  else:
      print("Found some mess but not a battery")
elif where == "in the bathroom":
  print("Where in the bathroom should I look?")
  look = input()
  if (look == "in the bathroom"):
    print("Found a rubber duck but not a battery")
  else:
      print("Found a wet surface but not a battery")
elif where == "in the lab":
  print("Where in the lab should I look?")
  look = input()
  if (look == "on the table"):
    print("Yes! I found my battery")
  else:
      print("Found some tools but not a battery")
else:
  print("I don't know where that is but I will keep looking")