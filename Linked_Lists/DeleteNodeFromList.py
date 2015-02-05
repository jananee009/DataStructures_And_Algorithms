# Implement an algorithm to delete a node in the middle of a single linked list, given access only to that node. 
# Approach: When you have access only to the node to be deleted, then copy the data from the next node to the current node and delete the next node, since it becomes a duplicate node.


import SinglyLinkedList as sll



def deleteNodeFromMiddle(p2):
	# p2 points to the 
	# copy the data from the next node to the current data.
	p2.setData(p2.getNext().getData())
	# Now, the current node and next node both have the same data.

	# delete the next node.
	p2.setNext(p2.getNext().getNext())
	return





def main():
	# Create a singly linked list with duplicates
	myList = sll.SingleLinkedList()

	myList.insertNode(100)
	myList.insertNode(200)
	myList.insertNode(300)
	myList.insertNode(400)
	myList.insertNode(500)
	myList.insertNode(600)
	myList.insertNode(700)
	print "Linked List:"
	myList.printLinkedList()

	# We want to delete node that has data 400. Move the pointer to the node with data 400.
	p1 = myList.head
	while(p1.getData() != 400):
		p1 = p1.getNext()
	# p1 now points to the node to be deleted. 	
	deleteNodeFromMiddle(p1)
	print "After node deletion:"
	myList.printLinkedList()	


	



if __name__ == "__main__":
	main()