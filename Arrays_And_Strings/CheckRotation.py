# Assume that you have a method to find out if one string is a subset of another one. You are given two strings s1 and s2.
# Write a method to find out if s2 is a rotation of s1 using only one call to the method. 
# For e.g. 'erbottlewat' is a rotation of 'waterbottle'.

def checkRotation(inputstr1, inputStr2):
	if (len(inputstr1) != len(inputStr2)):
		return False
	temp = inputStr2 + inputStr2
	if inputstr1 in temp:
		return True
	else:
		return False	


def main():
	user_input1 = input('Enter a string: ')
	user_input2 = input('Enter another string: ')
	print "You entered: ",user_input1, "and ",user_input2
	if(checkRotation(user_input1, user_input2)):
		print user_input2, " is a rotation of  ",user_input1
	else:
		print user_input2, " is NOT a rotation of  ",user_input1	


if __name__ == "__main__":
	main()