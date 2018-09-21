# Handell Desulme Section 4 Lab2
# This program will process a list of scores based on ids and print a list of grades for each id

#functions
def validate_input(num):
  if num > 0:
    return True
  else:
    print("Invalid Entry (integer must be greater than 0)")
    return False
  
  #no need to validate whether input is an actual integer in this program

def assign_grades(scores): #for loop here, for score in scores

  average = sum(scores)/len(scores)

  for score in scores:
    if score >average+10:
      grades.append("A")
    elif score>average+5:
      grades.append("B")
    elif score>average-5:
      grades.append("C")
    elif score>average-10:
      grades.append("D")
    else:
      grades.append("F")

def print_grades():
  for i in range(0,len(grades)):
    print(ids[i],"-",scores[i],"-",grades[i])
    print("_________________")
    print()

#initialize lists
ids = []
scores = []
grades = []

#sentinel value
stop = 0

#program
oneid = int(input("Please enter an integer greater than 0: "))
if validate_input(oneid):
  #run program
  while (oneid) > stop:
    ids.append((oneid))
    scores.append(float(input("Please enter a score between 0.00 and 100.00: ")))
    oneid = int(input("Please enter another integer (enter 0 to stop): "))

  assign_grades(scores)

  print_grades()


