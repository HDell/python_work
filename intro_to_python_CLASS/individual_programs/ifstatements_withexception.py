try: 
	key = eval(input("Enter a number between 1 and 5 (inclusive):"))
	if type(key) != type(0):
		print("You've entered a: ")
		print(type(key))
		print("\nPlease enter an int.")
except ValueError:
	print("You've entered a: ")
	print(type(key))
	print("\nPlease enter an int.")
	exit()


if key == 1 or key == 2 or key == 3 or key == 4 or key == 5:
	print("Correct")
elif key == 0 or key == 6 or key == 7:
	print("You're close")
elif key < 0:
	print("Please enter a positive integer")
else:
	print("You've entered a value that is too high")