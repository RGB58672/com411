def search(file_name):
  print("Searching...")
  sections = []
  books = []
  with open(file_name) as file:
    for line in file:
      if line.startswith("Section"):
        line.split(":")