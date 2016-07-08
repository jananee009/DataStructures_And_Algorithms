# Problem 94:  Write an efficient function that checks whether any permutation  of an input string is a palindrome .
# Source: https://www.interviewcake.com/question/javascript/permutation-palindrome
# Approach: A string can contain either even or odd number of alphabets in it. 
# A string with even number of letters is a palindrome if each letter occurs exactly even number of times. 
# A String with odd number of letters is a palindrome if except for one letter (which occurs odd number of times), all other letters occur exactly even number of times. 
# Algorithm:
# 1. Count the number of times each character appears in the input string ( in a dictionary char:count)
# 2. If the length of the string is even:
		# a. check the count of each character from the dictionary. 
		# b. if there is any count value that is odd, the string cannot be  a palindrome. 
# 3. If the length of the string is odd:		
		# a. check the count of each character from the dictionary. 
		# b. track the number of times odd count values appear. If this number exceeds one, the string cannot be a palindrome.




		

# given an input string, this function returns True if the string is a palindrome, else it returns false. 
def checkPalindrome(inputString):
	letterCount = {}

	# count number of times each alphabet is occurring in the inputstring.
	for letter in inputString.lower(): # convert input string to lwoercase before processing.
		if letter not in letterCount:
			letterCount[letter] = 1
		else:
			letterCount[letter] += 1

	if 	len(inputString) % 2 == 0: # string has even number of letters
		for eachValue in letterCount.values(): # if any letter occurs odd number of times, the string cannot be a palindrome. 
			if eachValue % 2 != 0:
				return False
			else:
				return True
	else: # string has odd number of letters
		number_of_letters_occurring_odd_number_of_times = 0
		for eachValue in letterCount.values():
			if eachValue % 2 == 0:
				continue
			else:
				number_of_letters_occurring_odd_number_of_times += 1
				
		
		if 	number_of_letters_occurring_odd_number_of_times == 1:
			return True
		else:
			return False		 
						


		
def main():
	print checkPalindrome("jananee")



if __name__ == "__main__":
	main()	
	


