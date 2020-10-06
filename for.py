print ("Please enter your name")
name = input()

if (len(name) < 6):
  for character in name:
    print(character)
else:
  print("You have a long name!")

for character in name:
  print(character)

# range
# - start index (included)
# - end index (excluded)
# - step (difference)
for value in range (1, 10, 1):
  print(value)