# Implement a program to reverse a string.
# Follow up: Write a function to reverse an array of characters in place. "In place" means "without creating a new string in memory."

def reverseString(inputStr):
	reversed = ""
	for i in range(len(inputStr)-1,-1,-1):
		reversed = reversed + inputStr[i]
	return reversed	


def reverseStringInPlace(inputStr):
	# python strings are immutable. i.e. once we create a string, we cannot change it.
	# To solve the problem, convert the string in to a list of characters and reverse the list in place. 
	# Then join all the characters in the list to get the reversed string
	listOfChar = [] # create a list of characters from the inputStr.
	listOfChar.extend(inputStr)
	temp = ''
	i=0
	j=len(listOfChar)-1
	while(i<j):
		temp = listOfChar[i]
		listOfChar[i] = listOfChar[j]
		listOfChar[j] = temp
		i = i+1
		j = j-1
	inputStr = ''.join(listOfChar)	
	return  inputStr	



def main():
	user_input = input("Enter a string: ")
	print "You entered: ",user_input 
	result1 = reverseString(user_input)
	print "Reversed string: ",result1
	result2 = reverseStringInPlace(user_input)
	print "Reversed string: ",result2

if __name__ == "__main__":
	main()