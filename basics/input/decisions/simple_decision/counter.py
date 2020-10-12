print("Please enter the first whole number:")
first = int(input())
print("Please enter the second whole number:")
second = int(input())
print("Please enter the third whole number:")
third = int(input())
odd_numbers = 0
even_numbers = 0
if (first % 2 == 0):
  even_numbers += 1
else:
  odd_numbers += 1
if (second % 2 == 0):
  even_numbers += 1
else:
  odd_numbers += 1
if (third % 2 == 0):
  even_numbers += 1
else:
  odd_numbers += 1
print("There are {} even and {} odd numbers".format(even_numbers,odd_numbers))