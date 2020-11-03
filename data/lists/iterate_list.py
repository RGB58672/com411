def get_directions():
  directions = ["Move Forward", "Move Backwards", "Move Left", "Move Right"]
  return directions

def menu():
  print("Please select a direction:")
  direction = get_directions()
  for index in range(len(direction)):
    print("{}:{}".format(direction[index],index))

def run():
  menu()

run()

