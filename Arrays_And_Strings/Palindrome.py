# Implement a method to check if a string is a palindrome.

def checkPalindromeWithNoDS(inputStr):
# Method checks if string is a palindrome without using additional  data structure.	
	j=len(inputStr)-1
	for i in range(0,len(inputStr)):
		if(i<j):
			if(inputStr[i]==inputStr[j]):
				j= j-1
			else:
				return False
		else:
			return True			

def checkPalindrome(inputStr):
	# reverse the given string. If the reversed string is same as original, the given string is a palindrome.
	reversed = ""
	for i in range(len(inputStr)-1,-1,-1):
		reversed = reversed + inputStr[i]
	if (inputStr == reversed):
		return True
	else:
		return False		



def main():
	user_input = input("Enter a string: ")
	print "You entered: ", user_input
	input_str = user_input.lower()
	if(checkPalindrome(input_str)):
		print user_input+" is a palindrome."
	else:
		print user_input+" is NOT a palindrome."	
	if(checkPalindromeWithNoDS(input_str)):
		print user_input+" is a palindrome."
	else:
		print user_input+" is NOT a palindrome."		
	


if __name__ == "__main__":
	main()