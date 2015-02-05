'''
Source: https://www.interviewcake.com/question/bracket-validator
Question: Write a braces/brackets/parentheses validator.
Let's say:
'(', '{', '[' are called "openers."
')', '}', ']' are called "closers."
Write an efficient function that tells us whether or not an input string's openers and closers are properly nested.
Examples:
"{ [ ] ( ) }" should return true
"{ [ ( ] ) }" should return false
"{ [ }" should return false
'''

class Stack:
	def __init__(self):
		self.stackList = []
		count = 0

	def push(self,element):
		self.stackList.append(element)
		return

	def pop(self):
		element = self.stackList[len(self.stackList)-1]	
		del self.stackList[len(self.stackList)-1]
		return 	element

	def peek(self):
		return 	self.stackList[len(self.stackList)-1]	

	def size(self):	
		return len(self.stackList)


def bracketValidator(inputStr):
	list_Of_Openers = ['(','{','[',]
	list_Of_Closers = [')','}',']']	
	paren_opener = '('
	brace_opener = '{'
	bracket_opener = '['
	paren_closer = ')'
	brace_closer = '}'
	bracket_closer = ']'
	paren = (paren_opener,paren_closer)
	brace = (brace_opener,brace_closer)
	bracket = (bracket_opener,bracket_closer)
	openerStack = Stack() # This stack will hold all the openers encountered in the string.

	
	for i in range(0,len(inputStr)):
		if inputStr[i] in list_Of_Openers:
			openerStack.push(inputStr[i]) # if you encounter an opener, push it in to a stack.
		
		if (inputStr[i] in list_Of_Closers and openerStack.size() >= 1): # if you encounter a closer
			# identify the closer i.e. whether it is a parentheses, brace or a bracket. Then check if the top most element in the stack is a corresponding opener. 
			# If yes, then pop the stack.  
			if (inputStr[i] in paren):
				if(paren[0] == openerStack.peek()):
					openerStack.pop()
			elif(inputStr[i] in brace):	
				if(brace[0] == openerStack.peek()):
					openerStack.pop()
			elif(inputStr[i] in bracket):	
				if(bracket[0] == openerStack.peek()):
					openerStack.pop()
			else:
				return False							
		elif (inputStr[i] in list_Of_Closers and openerStack.size() < 1):  # if  ), } or ] is encountered before any openers, return False
			return False	
		else:
			pass	

	if(openerStack.size() == 0):
		return True
	else:
		return False			



def main():
	user_input = input('Enter a string with validators: ') # input e.g. '[{(]})','[(){}]', '[{()}]', '{()}[]',  "{ [ ( ] ) }"
	print "You entered: ",user_input
	if(bracketValidator(user_input)):
		print "Good Nesting!!"
	else:
		print "Bad Nesting!!"	



if __name__ == "__main__":
	main()		

