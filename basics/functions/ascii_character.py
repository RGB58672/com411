print("Program Started!")
print("Please enter an ASCII code:")
code = int(input())
if (code >= 32 and code <= 126):
  print("The character {} has the ASCII value of {}".format(code,chr(code)))
else:
  print("Please enter a valid character")
print("The program has ended.")
