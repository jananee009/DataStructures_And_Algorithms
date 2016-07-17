# Write a function that, given a sentence, , finds the position of an opening parenthesis and the corresponding closing parenthesis.
# Source: https://www.interviewcake.com/question/python/matching-parens?utm_source=weekly_email&__s=ibuidbvzaa2i67rfb2mc
# Approach: 1. Process the string character by character.  
# We can solve the problem using a dictionary  and a stack (list).
# 2. As you encounter a parentheses, check if it is opening or closing one:
# 3. If it is opening one, find its position in the string and store it as a key in the dictionary. 
#  		 Push the position of the last found open parentheses in to a stack.
# 		At any point in time, the position of the most recently found  open parentheses can be obtained by popping the stack.
# 4. else if parentheses is a closing one:
#		pop the stack. i.e. get the position of the open parentheses that was most recently found and for which the corresponding closing parentheses was not found.
#		store the position of the closing parentheses as value for the key whose value is same as the popped value.





		

# this method uses a dictionary and a list to find the positions of opening and corresponding closing parentheses.
def findParentheses(inputString):
	last_found_open_parentheses = [] # this will be used like a stack.
	parentheses_dict = {}
	for index, character in enumerate(inputString):
		if character == "(":
			parentheses_dict[index]	= -1 
			last_found_open_parentheses.append(index)
		elif character == ")":
			if last_found_open_parentheses: # if last_found_open_parentheses is not empty
				parentheses_dict[last_found_open_parentheses[-1]] = index
				del last_found_open_parentheses[-1]	
			else:
				print "String with invalid parentheses"	
				return
	return 	parentheses_dict		
						


		
def main():
	sentence = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
	print findParentheses(sentence)



if __name__ == "__main__":
	main()	
	


