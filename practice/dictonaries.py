characters = {}
for i in range(3):
  print("What character would you like to input?")
  name = input()
  print("What show do they come from?")
  show = input()
  characters[name]= show
print(characters)
print(characters["Bender"])
for key, value in characters.items():
  print(f"{key} is from the show {value}")