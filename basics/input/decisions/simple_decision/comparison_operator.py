print("Please enter the first number")
first = int(input())
print("Please enter the second number")
second = int(input())
if (first > second):
  print("{} is bigger than {}".format(first,second))
elif (second > first):
  print("{} is smaller than {}".format(first,second))
else:
  print("Both numbers are equal")