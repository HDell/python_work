# Handell Desulme Section 4 Lab1
# This program will return lines from the song "days of Christmas" based on user input

# Validate Function
def validate(num_string):
  
  # check length of user input
  if len(num_string) != 1:
    print("Invalid input! Enter a single digit number!")
    return False

  # check if value is valid (from 1 to 5)
  if num_string in num_list:
    return True

  # number is invalid!
  print("Invalid input! Enter an integer from 1 to 5!")
  return False

def print_one_line(num_string):
  num = int(num_string)

  if num == 5:
    print("5 golden rings")
  elif num == 4:
    print("4 calling birds")
  elif num == 3:
    print("3 French hens")
  elif num == 2:
    print("2 turtle doves")
  elif num == 1:
    print("1 partridge in a pear tree.")
  return True

def print_many_lines(num_string):
  num = int(num_string)

  if num == 5:
    print("5 golden rings")
    print("4 calling birds")
    print("3 French hens")
    print("2 turtle doves")
    print("1 partridge in a pear tree.")
  elif num == 4:
    print("4 calling birds")
    print("3 French hens")
    print("2 turtle doves")
    print("1 partridge in a pear tree.")
  elif num == 3:
    print("3 French hens")
    print("2 turtle doves")
    print("1 partridge in a pear tree.")
  elif num == 2:
    print("2 turtle doves")
    print("1 partridge in a pear tree.")
  elif num == 1:
    print("1 partridge in a pear tree.")
  return True

# Check string against this list
num_list = "12345"

# Part A
num_string = (input("Enter a number from one to five: "))
if validate(num_string):
  print_one_line(num_string)

# Part B
num_string = (input("Enter another number from one to five: "))
if validate(num_string):
  print_many_lines(num_string)



