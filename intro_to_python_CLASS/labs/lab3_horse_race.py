# Handell Desulme Section 4 Lab3
# This program will 

import random

#functions
def validate_input(num):
  pass

def random_number_generator(list_arg):
  for i in range(0,1000):
    list_arg.append(random.randrange(10,21))
  print(len(list_arg))
  average = sum(list_arg)/len(list_arg)
  print("The mean of the random ints is:", average)

def one_horse_race(list_arg):
  seconds = 0
  while sum(list_arg) < miles_in_feet:
    list_arg.append(random.randrange(4,41))
    seconds = seconds + 1
  print("seconds for 1 horse, 1 race:", seconds)
  print("length of the list is:", len(list_arg))
  print("feet ran by horse is:", sum(list_arg))

#1 horse, multiple races

#multiple horses, 1 race

#multiple horse names, 1 race

#initializations
rand_number_list = []
horse_one = []
miles_in_feet = 10560

#program

random_number_generator(rand_number_list)
one_horse_race(horse_one)


