# Handell Desulme Section 4 Lab2
# This program will process a list of scores based on ids and print a list of grades for each id

import random

#functions
def validate_input(num):
  pass

def calculate_average(list_arg):
 pass

def random_number_generator(list_arg):
  for i in range(0,1000):
    list_arg.append(random.randrange(10,21))
  print(len(list_arg))
  average = sum(list_arg)/len(list_arg)
  print(average)

#1 horse, 1 race
  #random.randrange(4,41) feet / second --- add to list
  #check if total feet = 10560 [2 miles]
  #print("seconds for 1 horse, 1 race: ", seconds) #seconds = len(list)

#initializations
first_number_list = []

#sentinel value
stop = 0

#program

random_number_generator(first_number_list)


