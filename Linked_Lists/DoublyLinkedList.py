# Create a Doubly Linked List. Implement insert, search and delete operations.

class Node:
	def __init__(self,_data,_next,_prev):
		self.data = _data
		self.next = _next
		self.prev = _prev

	def setData(self,Data):
		self.data = Data
		return

	def getData(self):
		return self.data

	def setNext(self,Next):
		self.next = Next
		return

	def getNext(self):
		return self.next


	def setPrev(self,Prev):
		self.prev = Prev
		return

	def getPrev(self):
		return self.prev


class DoublyLinkedList:
	def __init__(self):
		self.count = 0
		self.head = Node(None,None,None)

	def insertNode(self,value):
		# adds a new node at the end of the list.
		newNode = Node(value,None,None)					
		self.curr = self.head
		while(self.curr.getNext() != None):
			self.curr = self.curr.getNext()
		newNode.setPrev(self.curr)	
		self.curr.setNext(newNode)
		self.count = self.count + 1
		return		

	def searchNode(self,value):
		if(self.count<1):
			print "Linked list is empty. Nothing to find here."
			return False	
		counter = 0
		self.curr = self.head
		while(self.curr.getNext() != None):
			self.curr = self.curr.getNext()	
			print self.curr.getData()
			counter = counter + 1
			if (self.curr.getData() == value):
				print "Node with value: ", value, " found at position: ", counter
				return True
		print "Node with value: ", value, " not found."		
		return False	


	def deleteNode(self,value):
		if(self.count < 1):
			print "Linked list is empty. Nothing to delete here."
			return False
		self.curr = self.head
		while(self.curr.getNext() != None):
			self.curr = self.curr.getNext()	
			print self.curr.getData()
			if(self.curr.getData() == value):
				if(self.curr.getNext() != None):
					self.curr.getPrev().setNext(self.curr.getNext())
					self.curr.getNext().setPrev(self.curr.getPrev())
				else:
					self.curr.getPrev().setNext(None)
				self.count = self.count - 1
				print "Node with value: ", value, " deleted." 
				return True
		print "Node with value: ", value, " not found."			
		return False

	def getSize(self):
		print "Size of linkedlist is: ",self.count
		return self.count	

	def printLinkedList(self):
		self.curr = self.head
		linkedlistStr = ""
		linkedlistStr = linkedlistStr+"Head "
		while(self.curr.getNext() != None):
			linkedlistStr = linkedlistStr +  " <--> " 
			self.curr = self.curr.getNext()	
			linkedlistStr = linkedlistStr + str(self.curr.getData())
		linkedlistStr = linkedlistStr + " <--> "
		linkedlistStr = linkedlistStr + "None"
		print linkedlistStr
		return		

def main():
	myDoublyLinkedList = DoublyLinkedList()
	myDoublyLinkedList.insertNode(100)
	myDoublyLinkedList.insertNode(200)
	myDoublyLinkedList.insertNode(300)
	myDoublyLinkedList.insertNode(400)
	myDoublyLinkedList.insertNode(500)
	myDoublyLinkedList.insertNode(600)
	myDoublyLinkedList.getSize()
	myDoublyLinkedList.printLinkedList()

	myDoublyLinkedList.deleteNode(600)
	myDoublyLinkedList.getSize()
	myDoublyLinkedList.printLinkedList()
	

if __name__ == "__main__":
	main()							


