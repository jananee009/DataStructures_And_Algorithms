# Implement a program to reverse a string.

def reverseString(inputStr):
	reversed = ""
	for i in range(len(inputStr)-1,-1,-1):
		reversed = reversed + inputStr[i]
	return reversed	



def main():
	user_input = input("Enter a string: ")
	print "You entered: ",user_input 
	result = reverseString(user_input)
	print "Reversed string: ",result

if __name__ == "__main__":
	main()