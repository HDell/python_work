# Handell Desulme Section 4 Lab3
# This program will 

import random

#functions
def validate_input(num):
  if num > 1:
    return True
  else:
    print("Invalid Entry (integer must be greater than 0)")
    return False

def random_number_generator():
  rand_number_list = []
  for i in range(0,1000):
    rand_number_list.append(random.randrange(10,21))
  print(len(rand_number_list))
  average = sum(rand_number_list)/len(rand_number_list)
  print("The mean of the random ints is:", average)

def getKey(list_item):
  return list_item[0]

def one_horse_one_race():
  horse_miles = []
  seconds = 0
  while sum(horse_miles) < miles_in_feet:
    horse_miles.append(random.randrange(4,41))
    seconds = seconds + 1
  print("seconds for 1 horse, 1 race:", seconds)
  print("length of the list is:", len(horse_miles))
  print("feet ran by horse is:", sum(horse_miles))

def one_horse_multiple_races():
  horse_miles = []
  average_seconds = []
  seconds = 0
  for i in range(0,1000):
    while sum(horse_miles) < miles_in_feet:
      horse_miles.append(random.randrange(4,41))
      seconds = seconds + 1
    average_seconds.append(seconds)
    horse_miles.clear()
    seconds = 0
  average = sum(average_seconds)/len(average_seconds)
  print("The average number of seconds for horse to complete race is:", average)

def multiple_horses_one_race():
  horse_list = [] #[(distance, horse #),(distance, horse #),(distance, horse #),(distance, horse #)]

  distances = []
  seconds = 0
  num_horses = 0
  race_won = False
  winners = []
  ordered_winners = []

  num_horses = int(input("Please enter the number of horses in this race (greater than 1): "))
  if validate_input(num_horses):
    for i in range(0,num_horses):
      distances.append(0)
    while race_won == False:
      for i in range(0,num_horses):
        distances[i] = distances[i] + random.randrange(4,41)
        if distances[i] >= miles_in_feet:
          race_won = True
          winners.append((distances[i],i+1))
      seconds = seconds + 1
      if seconds%10 == 0:
        print(distances, seconds)
    ordered_winners = (sorted(winners, key=getKey, reverse=True))
    print(sorted(winners, key=getKey, reverse=True))

    print("The winning horse is horse number",ordered_winners[0][1],"with a distance of",ordered_winners[0][0],"miles!")

    print(distances, seconds)



    
    

    



#multiple horse names, 1 race

#initializations
miles_in_feet = 10560

#program

random_number_generator()
one_horse_one_race()
one_horse_multiple_races()
multiple_horses_one_race()

