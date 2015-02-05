# Write a program to implement a queue (FIFO). Implement the operations : enqueue, dequeue, peek.

class Queue:
	def __init__(self):
		self.queue = []

	def isEmpty(self):
		if(len(self.queue)==0):
			print "Queue is empty."
			return True
		else:
			print "Queue is not empty."
			return False

	def enqueue(self,element):
		self.queue.append(element)

	def dequeue(self):
		if(len(self.queue)==0):
			print "Queue is Empty. Nothing to dequeue."
			return
		tmp = self.queue[0]
		del self.queue[0]
		print "Popped element: ",tmp
		return tmp

	def peek(self):
		if(len(self.queue)==0):
			print "Queue is Empty."
			return		
		print "element that will be popped next is: ",	self.queue[0]	
		return self.queue[0]	

	def getSize(self):
		print "Size of Queue: ", len(self.queue)
		return len(self.queue)


def main():
	myQueue = Queue()
	myQueue.enqueue(10)
	myQueue.enqueue(20)
	myQueue.isEmpty()
	myQueue.getSize()
	myQueue.enqueue(30)
	myQueue.peek()
	myQueue.dequeue()
	myQueue.peek()
	myQueue.dequeue()
	myQueue.dequeue()
	myQueue.dequeue()
	myQueue.isEmpty()
	myQueue.getSize()	



if __name__ == "__main__":
	main()




	