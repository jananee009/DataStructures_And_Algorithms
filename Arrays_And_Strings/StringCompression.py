# Implement a program to perform basic string compression using the counts of repeated characters. 
# For e.g., the string aaaabbbccd will be compressed as a4b3c2d1. 
# If the compressed string would not become smaller than the original, then return the original string. 

# Approach: Read each character of the input string. Have a counter. Compare each subsequent character with previous character. 
# Keep incrementing counter until they are the same. Once different, store the character and its count in a separate string. 
# Repeat this process until you reach end of the string. 



def stringCompress(inputStr):
	inputStr = inputStr.strip()
	lastChar = inputStr[0]
	count = 1
	compressed = ""

	for i in range(1,len(inputStr)):
		if (inputStr[i]==lastChar):
			count = count + 1
		else:
			compressed = compressed + lastChar + str(count)
			lastChar = inputStr[i]
			count = 1
	print compressed		
	return compressed		
				








def main():
	user_input = input('Enter a string: ')
	print "You have entered: ", user_input
	result = stringCompress(user_input)
	if len(result) < len(user_input):
		print "Compressed string is: ",result
	else:
		print "Compressed string is longer than original string. Hence you get back your original string: ",user_input	 



if __name__ == "__main__":
	main()