#Question: Imagine a literal stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would like to start a new stack 
# when the previous stack exceeds some threshold. 
# Implement a datastructure SetOfStacks that mimics this. SetOfStacks must be composed of several stacks and should 
# create a new stack once the previous one exceeds capacity.
# SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack i.e. that is pop() should return the same values as it would 
# if there were just a single stack.

# Source : Cracking the coding interview by Gayle Laakmann McDowell.

# Approach: We will have one main stack. This main stack will have multiple stacks. Assume each stack can hold up to a maximum of 3 elements. 


import Stack as stk

class SetOfStacks:
	def __init__(self):
		self.threshold = 3
		self.numberOfStacks = 0
		self.numberOfItemsInTopStack = 0
		self.stackSet = stk.Stack()  # create the main stack. 
				


	
	def push(self,plate):
		if (self.stackSet.getSize() < 1): # main stack is empty or 
			self.newStack = stk.Stack()   # create a new stack. 
			self.newStack.push(plate) # push item in to stack
			self.stackSet.push(self.newStack) # push the newly created stack in to the main stack. 
			#self.numberOfStacks  = self.numberOfStacks  + 1 # increment the stack count by 1.
		else: 	# main stack is not empty
			 if (self.stackSet.peek().getSize() >= self.threshold):   # top most stack in main stack is full.
			 	self.newStack = stk.Stack()  #create a new stack 
				self.newStack.push(plate) # push item in to stack
				self.stackSet.push(self.newStack) # push the newly created stack in to the main stack. 
				#self.numberOfStacks  = self.numberOfStacks  + 1 # increment the stack count by 1.
			 else: # top most stack in main stack has some room for more items
				temp = self.stackSet.pop() # get the top most stack from main stack.
				temp.push(plate) # push the item in to the stack.
				self.stackSet.push(temp) # push the stack back in to main stack.
		return		



	def pop(self):
		if (self.stackSet.isEmpty()): # main stack is empty
			print "Stack Set is empty. Nothing to pop!"
			return
		temp = self.stackSet.pop()	# get the top most stack from main stack.
		if (not temp.isEmpty()): # top most stack is not empty
			plate = temp.pop() #pop the top most element from the topmost stack.
			if( not temp.isEmpty()): # if the top most stack doesnt become empty after popping 
				self.stackSet.push(temp) # push the stack back in to main stack. 
			else: 
				pass
				# dont do anything
		return plate			


	def getStackSetSize(self):
		return 	self.stackSet.getSize()





def main():
	mySet = SetOfStacks()
	mySet.push(1)
	mySet.push(2)
	mySet.push(3)
	print "size is: ",mySet.getStackSetSize()
	mySet.push(4)
	mySet.push(5)
	mySet.push(6)
	mySet.push(7)
	mySet.push(8)
	print "size is: ",mySet.getStackSetSize()
	print "popping: ",mySet.pop()
	print "popping: ",mySet.pop()
	print "size is: ",mySet.getStackSetSize()




if __name__ == "__main__":
	main()		

		


