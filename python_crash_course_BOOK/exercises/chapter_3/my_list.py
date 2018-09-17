fruits = ['orange', 'apple', 'pear', 'mango']

def my_fav(fruit_name):
  print(fruit_name + "s are my favorite fruit!")

for fruit in fruits:
  my_fav(fruit.title())

print(fruits)
print(len(fruits))

fruits.append('grape')

print(fruits)
print(len(fruits))

grape = fruits.pop()
print(grape)

print(fruits)
print(len(fruits))

fruits.remove('pear') #find and remove the item containing 'pear' in the list
del fruits[0] #remove the first object ('orange')

print(fruits)
print(len(fruits))

