# Question: Use your Stack class to implement a new class MaxStack with a function get_max() that returns the largest element in the stack. 
# get_max() should not remove the item. Your stacks will contain only integers.
# Source: https://www.interviewcake.com/question/python/largest-stack?utm_source=weekly_email

# Approach: We will keep 2 stacks. The first stack will hold all our elememts in the order they come in. 
# We will use the second stack to track  max elements. 
# So, if a element comes in, we will push it in to stack1. if element > topmost element in stack2, we will push the element in to stack2. 
# At any point, if we want to get the max element in a stack, we peek in to stack2. 
# When we pop elements, we pop them from stack1. We check whether popped element == topmost element in stack2. 
# If it is, then it means we just popped the maximum element from stack1. We need to pop the same element from stack2 as well. 
# Now, at this point, if we want max element, we will peek in to stack2.


import Stack as stk

class MaxStack:
	def __init__(self):
		self.originalStack = stk.Stack()  
		self.maxStack = stk.Stack()


	def push(self,element):
		self.originalStack.push(element)
		if self.maxStack.isEmpty(): 
			self.maxStack.push(element)
		elif element > self.maxStack.peek():
			self.maxStack.push(element)

	def pop(self):
		if self.originalStack.peek() == self.maxStack.peek(): # Max element is being popped. 
			self.maxStack.pop()
			return self.originalStack.pop()
		else:
			return self.originalStack.pop()
				

	def get_max(self):
		return self.maxStack.peek()

	
	def isEmpty(self):
		if self.originalStack.isEmpty():
			return True
		else:
			return False			


def main():
	myMaxStack = MaxStack()
	myMaxStack.push(5)
	myMaxStack.push(8)
	myMaxStack.push(3)
	myMaxStack.push(2)
	myMaxStack.push(10)
	myMaxStack.push(1)
	

	while not myMaxStack.isEmpty(): 

		print "popping: ",myMaxStack.pop()
		print "max value is: ",myMaxStack.get_max()
		
	
	


if __name__ == "__main__":
	main()		

		


