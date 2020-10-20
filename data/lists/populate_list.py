def directions():
  directions = ["Move Forward", "Move Backwards", "Move Left", "Move Right"]
  return directions
def menu():
    print("Please select a direction:")
    direction = directions()
    for index in range(len(direction)):
      print("{}:{}".format(direction[index],index))
    user_choice = int(input())
    return direction[user_choice]
def run():
  route = []
  print("Working out escape route...")
  for count in range(5):
    direction = menu()
    route.append(direction)
  print("Escape route: {}".format(route))

run()
