# Write a program to implement a stack (LIFO). Implement the operations : push, pop, peek.

class Stack:
	def __init__(self):
		self.stack = []

	def isEmpty(self):
		if(len(self.stack)==0):
			return True
		else:
			return False

	def push(self,element):
		self.stack.append(element)

	def pop(self):
		if(len(self.stack)==0):
			print "Empty!! Nothing to pop."
			return
		tmp = self.stack[len(self.stack)-1]
		del self.stack[len(self.stack)-1]
		return tmp

	def peek(self):
		if(len(self.stack)==0):
			return "Empty stack."		
		return self.stack[len(self.stack)-1]	

	def getSize(self):
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




	