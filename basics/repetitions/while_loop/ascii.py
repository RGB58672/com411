print("How many bars should be charged?")
bars = int(input())
charged_bars = 0
while (charged_bars < bars):
  charged_bars += 1
  print("Charging...")
  print("#" * charged_bars)