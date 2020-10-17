print("Please enter a sequence")
sequence = input()
print("Please enter the character for the marker")
marker = input()
is_counting = False
count = 0
for character in sequence:
  if (character == marker and is_counting == True):
    print("found last marker")
  elif (character == marker and is_counting == False):
    print("found first marker")
    is_counting = True
  elif (character != marker and is_counting == True):
    count += 1
print("The distance is {}. ".format(count))