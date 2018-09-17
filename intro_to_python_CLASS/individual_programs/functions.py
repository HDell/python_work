def sum_five_nums(val1,val2,val3,val4,val5):
	sum = val1+val2+val3+val4+val5
	return sum

def isInt(expr):
	if type(expr) == type(0): # return type(expr) == type(0)
		return_val = True
	else:
		return_val = False
	return return_val

if __name__ == "__main__": #__name__ would equal the name of the python library (file name) if the file was called from out of the __name__
	x = 10
	y = 3.14
	z = "dog"
	print(__name__)

	val = sum_five_nums(5,5,5,5,5)

	print(val)

	print(x, isInt(x))
	print(y, isInt(y))
	print(z, isInt(z))

	print(type(type(3+5)))