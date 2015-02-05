# Write a program to implement a queue using 2 stacks.


import Stack as stk

class StackUsingQ:
	def __init__(self):
		self.myStack1 = stk.Stack()
		self.myStack2 = stk.Stack()

	def moveElements(self,stk1,stk2): # This method pushes all elements from stk1 to stk2.
		while(stk1.getSize() > 0):
			stk2.push(stk1.pop())	
		return	



	def pushElement(self,element): # This method pushes all elements to stack1.
		self.myStack1.push(element)
		return

	def popElement(self):
		if(self.myStack1.getSize() == 0):
			return

		self.moveElements(self.myStack1,self.myStack2) # push all elements from stack 1 to stack 2.
		value = self.myStack2.pop() # Pop from the 2nd Stack. 
		print "Element popped is: ",value
		
		self.moveElements(self.myStack2,self.myStack1)	# push all elements from stack 2 to stack 1.

		return value


	def peekElement(self):
		if(self.myStack1.getSize() == 0):
			return
		
		self.moveElements(self.myStack1,self.myStack2) # push all elements from stack 1 to stack 2.
		self.myStack2.peek() # This is the first element of the queue		
		self.moveElements(self.myStack2,self.myStack1)	# push all elements from stack 2 to stack 1.
		return 			



def main():
	myQueue = StackUsingQ()
	myQueue.pushElement(3)
	myQueue.pushElement(2)
	myQueue.pushElement(1)
	myQueue.pushElement(4)

	myQueue.peekElement()

	myQueue.popElement()
	myQueue.pushElement(200)
	myQueue.pushElement(300)
	myQueue.popElement()
	myQueue.popElement()
	myQueue.popElement()
	myQueue.peekElement()
	myQueue.popElement()
	myQueue.popElement()
	myQueue.popElement()	



if __name__ == "__main__":
	main()




	