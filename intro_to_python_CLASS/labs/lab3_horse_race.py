# Handell Desulme Section 4 Lab3
# This program will progressivley simulate horse races.

import random

#functions
def validate_input(num):
  if num > 1:
    return True
  else:
    print("Invalid Entry (number (integer) of horses must be greater than 0)")
    return False

def random_number_generator(): #part a
  rand_number_list = []
  for i in range(0,1000):
    rand_number_list.append(random.randrange(10,21))
  print(len(rand_number_list))
  average = sum(rand_number_list)/len(rand_number_list)
  
  print("The mean of the random ints is:", average) #main output

def one_horse_one_race(): #part b
  horse_miles = []
  seconds = 0
  while sum(horse_miles) < miles_in_feet:
    horse_miles.append(random.randrange(4,41))
    seconds = seconds + 1
  
  print("seconds for 1 horse, 1 race:", seconds) #main output
  #print("length of the list is:", len(horse_miles)) #same as seconds
  #print("feet ran by horse is:", sum(horse_miles))

def one_horse_multiple_races(): #part c
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
  
  print("The average number of seconds for horse to complete race is:", average) #main output

def getKey(list_item):
  return list_item[0]

def multiple_horses_one_race(): #part e

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
    ordered_winners = (sorted(winners, key=getKey, reverse=True))
    #print(sorted(winners, key=getKey, reverse=True))

    print("The winning horse is horse number",ordered_winners[0][1],"with a distance of",ordered_winners[0][0],"feet in", seconds, "seconds!") #main output
    #print("The winning horse is horse number",ordered_winners[0][1],"with a distance of",ordered_winners[0][0]/(miles_in_feet/2),"miles in", seconds, "seconds!") #alt. output

    #print(distances, seconds)

def horse_names_one_race(): #part e

  distances = []
  seconds = 0
  horse_names = []
  horse_name = ""
  race_won = False
  winners = []
  sorted_winners = []

  horse_name = input("Please enter the name of the first competing horse in this race ('XXX is invalid'): ")
  while horse_name != "XXX":
    horse_names.append(horse_name)
    horse_name = input("Please enter the name of the next competing horse in this race (enter 'XXX' to stop): ")
  if validate_input(len(horse_names)):
    for i in range(0,len(horse_names)):
      distances.append(0)
    while race_won == False:
      for i in range(0,len(horse_names)):
        distances[i] = distances[i] + random.randrange(4,41)
        if distances[i] >= miles_in_feet:
          race_won = True
          winners.append((distances[i],horse_names[i]))
      seconds = seconds + 1
      if seconds%10 == 0:
        pass
        print(seconds, "seconds into the race, we have:")
        for i in range(len(horse_names)):
          print(horse_names[i], "at", distances[i], "feet") #secondary output
    sorted_winners = (sorted(winners, key=getKey, reverse=True))
    #print(sorted(winners, key=getKey, reverse=True))

    print("The winning horse is",sorted_winners[0][1],"with a distance of",sorted_winners[0][0],"feet in", seconds, "seconds!") #main output
    #print("The winning horse is",sorted_winners[0][1],"with a distance of",sorted_winners[0][0]/(miles_in_feet/2),"miles in", seconds, "seconds!") #alt. output


    #print(distances, horse_names, seconds)

    
    

    



#multiple horse names, 1 race

#initializations
miles_in_feet = 10560

#program

random_number_generator() #part a
one_horse_one_race() #part b
one_horse_multiple_races() #part c
multiple_horses_one_race() #part d
horse_names_one_race() #part e

