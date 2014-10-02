# Given two strings, write a program to find out if one is a permutation of the other.
# Approach: get all the unique characters and their count from each string. Compare the characters and count.


def checkPermutation(input1, input2):
	# if the 2 input strings are of different length, then they cannot be permutations of each other.
	if (len(input1) != len(input2)):
		return False
	dict1 = getCharCount(input1)
	dict2 = getCharCount(input2)

	# sort the dictionary by keys. The output of sorted function is a list of tuples.
	list1 = sorted(dict1.items())
	list2 = sorted(dict2.items())

	# Compare the lists. if they are equal, then 2 strings are permutations of each other.
	if(list1==list2):
		return True
	else:
		return False		


def getCharCount(inputStr):
	# create a dictionary of characters (keys) and the number of times they occur in the string (values).
	temp = dict()
	for i in range(0,len(inputStr)):
		if temp.has_key(inputStr[i]):
			temp[inputStr[i]] = temp[inputStr[i]] + 1
		else:
			temp[inputStr[i]] = 1	
	return temp		



def main():
	# Accept 2 strings from the user.
	user_input1 = input("Enter a string: ")
	user_input2 = input("Enter another string: ")
	print "You entered: ", user_input1, user_input2

	# Convert both strings to lower case. 
	first_str = user_input1.lower()
	second_str = user_input2.lower()


	if(checkPermutation(first_str,second_str)):
		print user_input1, "and", user_input2 , " ARE permutations of each other."
	else:
		print user_input1, "and", user_input2 , " ARE NOT permutations of each other."	


if __name__ == "__main__":
	main()
