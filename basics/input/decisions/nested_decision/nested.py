print("What kind of cover does the book have?")
cover = input()
if (cover == "soft"):
  print("Is the book pefect-bound?")
  response = input()
  if (response == "yes"):
    print("Soft cover, perfect bound books are very popular!")
  else:
    print("Soft covers with coils or stitches are great for short books")
else:
  print("Books with hard covers can be more expensive!")