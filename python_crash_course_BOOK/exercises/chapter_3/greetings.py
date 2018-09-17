friends = ['richard', 'faith', 'danni', 'jon']
#print("Hi " + friends[0].title() + ". Welcome to Python!")
#print("Hi " + friends[1].title() + ". Welcome to Python!")
#print("Hi " + friends[2].title() + ". Welcome to Python!")
#print("Hi " + friends[3].title() + ". Welcome to Python!")

def greet_friend(friend_name):
  print("Hi " + friend_name + ". Welcome to Python!")

for names in friends:
  greet_friend(names.title())

print(len(friends))

