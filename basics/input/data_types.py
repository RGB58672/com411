print("What is your name human?")
name = input()
print("How old are you (in years)?")
age = input()
print("How tall are you (in meters)?")
height = input()
print("How much do you weigh (in kilograms)?")
weight = input()
print(" " + name + " you are"  + age + " years old and your bmi is ") 

# Read in user data 
print("What is your name?")
name = input() 

print("What is your age?")
age = int(input())

print("What is your weight?") 
weight = float(input()) 

print("What is your height?")
height = float(input())

# Calculate bmi
bmi = weight / (height ** 2)

# Display result
print(name, "your bmi is", bmi