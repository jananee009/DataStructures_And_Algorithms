# Write a program to implement a stack (LIFO). Implement the operations : push, pop, peek.

class Stack:
	def __init__(self):
		self.stack = []

	def isEmpty(self):
		if(len(self.stack)==0):
			#print "Stack is empty."
			return True
		else:
			#print "Stack is not empty."
			return False

	def push(self,element):
		self.stack.append(element)

	def pop(self):
		if(len(self.stack)==0):
			print "Empty!! Nothing to pop."
			return
		tmp = self.stack[len(self.stack)-1]
		del self.stack[len(self.stack)-1]
		#print "Popped element: ",tmp
		return tmp

	def peek(self):
		if(len(self.stack)==0):
			print "Empty!! Nothing to peek!!"
			return		
		#print "element that will be popped next is: ",	self.stack[len(self.stack)-1]	
		return self.stack[len(self.stack)-1]	

	def getSize(self):
		#print "Size: ", len(self.stack)
		return len(self.stack)

	def printStack(self):
		print "printing elements:"
		for i in range(len(self.stack)-1,-1,-1):
			print self.stack[i]
		return		


def main():
	myStack = Stack()
	myStack.push(10)
	myStack.push(20)
	myStack.isEmpty()
	myStack.getSize()
	myStack.push(30)
	myStack.peek()
	myStack.pop()
	myStack.peek()
	myStack.pop()
	myStack.pop()
	myStack.pop()
	myStack.isEmpty()
	myStack.getSize()	



if __name__ == "__main__":
	main()




	