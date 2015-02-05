# write a program to implement a stack (LIFO) with operations push(), pop(), peek() and min(). All operations must functio in O(1) time. 
# 


class StackImpl:
	def __init__(self):
		self.stack = []
		self.minValue = 1000000000 # MAXint value
		self.minValueTracker = []
		

	def push(self,element):
		if(element < self.minValue):
			self.minValue = element
			self.minValueTracker.append(self.minValue)
		self.stack.append(element)
		return

	def pop(self):
		if(len(self.stack)<=0):
			print "Stack is empty."
			return

		tmp = self.stack[len(self.stack)-1]
		if(tmp == self.minValueTracker[len(self.minValueTracker)-1]):
			del self.minValueTracker[len(self.minValueTracker)-1]

		print "Element popped is: ",self.stack[len(self.stack)-1]
		del self.stack[len(self.stack)-1]
		return 

	def peek(self):
		if(self.count<0):
			print "Stack is empty."
			return	
		print "last element in stack is: ",	self.stack[len(self.stack)-1]
		return 			


	def getSize(self):
		return len(self.stack)	

	def getMinValue(self):
		print "Min value of stack is: ",self.minValueTracker[len(self.minValueTracker)-1]
		return 	


def main():
	myStack = StackImpl()
	myStack.push(40)
	myStack.push(30)
	myStack.push(20)
	myStack.push(10)
	myStack.push(100)
	myStack.push(200)
	myStack.push(300)
	myStack.getMinValue()
	myStack.pop()
	myStack.pop()
	myStack.pop()
	myStack.pop()
	myStack.getMinValue()	
	myStack.pop()
	myStack.getMinValue()	


if __name__ == "__main__":
	main()	

