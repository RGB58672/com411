print("What level of brightness is required?")
brightness = int(input())
print("Adjusting brightness...")
for brightness_setting in range(2, brightness + 1, 2):
  print("Beep's brightness level:", "*" * brightness_setting)
  print("Bop's brightness level:", "*" * brightness_setting)
print("Adjustments complete!")