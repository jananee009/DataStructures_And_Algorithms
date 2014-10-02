# Write a method to replace all spaces in a string with '%20'. Assume that the string has sufficient space at the end of the string to hold the additional characters
# and that you are given the true length  of the string. 
# E.g. Input: "Mr John Smith      ", 13
# Output: "Mr%20John%20Smith"

def replaceAllSpaces(input):
	newString = ""
	# Find each space in the input string. Replace it with '%20'.
	for i in range(0,len(input)):
		if(input[i] == " "):
			newString = newString + "%20"
		else:
			newString = newString + input[i]	
	return newString			



def main():
	user_input = input("Enter a string: " )
	print "You entered: ", user_input
	result = replaceAllSpaces(user_input)
	print "Result is: ",result 



if __name__ == "__main__":
	main()
