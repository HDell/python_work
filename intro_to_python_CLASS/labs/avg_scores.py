# Handell Desulme Section 4 Lab2
# This program will ...

#functions
def validate_input(num):
  if (num) > 0:
    return True
  else:
    print("Invalid Entry (integer must be greater than 0)")
    return False
  #check if it is an actual #

def assign_grade(score, average): #for loop here, for score in scores
  pass
  #return a grade

  #score > average+10 -> A
  #score > average+5 -> B
  #score > average-5 -> C
  #score > average-10 -> D
  #otherwise -> F

def print_grade():
  pass

#lists
ids = []
scores = []
grades = []

#sentinel value
stop = 0

#program
oneid = int(input("Please enter an integer greater than 0: "))
if validate(oneid):
  #run program
  while (oneid) > stop:
    ids.append((oneid))
    scores.append(float(input("Please enter a score between 0.00 and 100.00: ")))
    oneid = int(input("Please enter another integer: "))
