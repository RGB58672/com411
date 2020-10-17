print("What strange markings do you see?")
markings = input()
print("Identifying...")
for count in range (0, len(markings), 1):
  print("index", count, ":", markings [count])
print ("Process complete!")