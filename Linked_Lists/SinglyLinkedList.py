# Create a Single Linked List. Implement insert, search and delete operations.
class Node:
	def __init__(self, Data, Next):
		self.data = Data
		self.next = Next
		

	def setData(self, _data):
		self.data = value
		return

	def getData(self):
		return self.data

	def setNext(self, _next):
		self.next = _next
		return

	def getNext(self):
		return self.next


class SinglyLinkedList:
	def __init__(self):
		self.count = 0
		self.head = Node(None,None)

	def insertNode(self,value):
	# insert a node at the end of the list.
		newNode = Node(value,None)
		self.curr = self.head
		while(self.curr.getNext() != None):
			self.curr = self.curr.getNext()
		self.curr.setNext(newNode)
		self.count = self.count + 1
		return	


	def searchNode(self,value):
		if (self.count < 1):
			print "Linked list is empty. Nothing to find here."
			return False
		self.curr = self.head
		while(self.curr.getNext() != None):
			self.curr = self.curr.getNext()	
			if (self.curr.getData() == value):
				print "Node with value: ", value, " found."
				return True
		print "Node with value: ", value, " not found."		
		return False
		

	def deleteNode(self,value):
		if(self.count < 1):
			print "Linked list is empty. Nothing to delete here."
			return False
		self.curr = self.head
		while(self.curr.getNext() != None):
			if(self.curr.getNext().getData() == value):
				# the next node is the node to be deleted. 
				self.curr.setNext(self.curr.getNext().getNext())
				self.count = self.count - 1
				print "Node with value: ", value, " deleted." 
				return True
			else:
				self.curr = self.curr.getNext()	
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
			linkedlistStr = linkedlistStr +  " --> "
			self.curr = self.curr.getNext()	
			linkedlistStr = linkedlistStr + str(self.curr.getData())
		linkedlistStr = linkedlistStr + " --> "
		linkedlistStr = linkedlistStr + "None"
		print linkedlistStr
		return	


def main():
	myLinkedList = SinglyLinkedList()
	myLinkedList.insertNode(100)
	myLinkedList.insertNode(200)
	myLinkedList.insertNode(300)
	myLinkedList.insertNode(400)
	myLinkedList.insertNode(500)
	myLinkedList.insertNode(600)
	myLinkedList.getSize()
	myLinkedList.searchNode(200)
	myLinkedList.searchNode(1000)

	myLinkedList.deleteNode(300)
	myLinkedList.getSize()
	myLinkedList.searchNode(300)

	myLinkedList.deleteNode(600)
	myLinkedList.getSize()
	myLinkedList.searchNode(600)
	myLinkedList.printLinkedList()






if __name__ == "__main__":
	main()



