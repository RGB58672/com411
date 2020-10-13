print("How many live cables should I avoid?")
cables = int(input())
live_cables = 0
while (live_cables < cables):
  live_cables += 1
  print("Avoiding...Done! {} live cables avoided.".format(live_cables))