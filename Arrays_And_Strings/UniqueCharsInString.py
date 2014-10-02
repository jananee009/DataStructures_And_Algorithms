# Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

import sys
#print sys.argv

def isUnique(input):
	temp = []
	for i in range(0,len(input)):
		if input[i] in temp:
			return False
		else:
			temp.append(input[i])	
	return True		


def isUniqueNoDS(input):
# This method checks if the input string has unique characters without using any additional data structures.
	for i in range(0,len(input)):
		for j in range(i+1,len(input)):
			if (input[i] == input[j]):
				return False
	return True					



def main():
	user_input = input("Enter a string: ")
	print "You entered: ", user_input
	input_str = user_input.lower()
	if(isUnique(input_str)):
		print user_input+" has unique characters."
	else:
		print user_input+" does not have unique characters."	
	if(isUniqueNoDS(input_str)):
		print user_input+" has unique characters."
	else:
		print user_input+" does not have unique characters."		
	


if __name__ == "__main__":
	main()