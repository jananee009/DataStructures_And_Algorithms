# Problem: Write a code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.
# Approach: We are given a single linked list. Create 2 new single linked list. One will hold nodes less than x and the other one will hold nodes greater than or equal to x.
# Iterate through the given linked list. Add elements to the 2 new lists accordingly. Then merge both the lists together to get one list.

import SinglyLinkedList as sll


def partitionList(linkedlist,x):
	if(linkedlist.getSize() < 1): # Error check
		print "Linked list is empty."
		return
	# create 2 empty linked lists to store nodes less than and greater than equal to x.	
	lessThan = 	sll.SingleLinkedList()
	greaterThan = sll.SingleLinkedList()
	curr = linkedlist.head
	# Iterate through the given list and add nodes to the new lists depending upon their value.
	while (curr.getNext() != None):
		curr = curr.getNext()
		if(curr.getData() < x):
			lessThan.insertNode(curr.getData())
		else:
			greaterThan.insertNode(curr.getData())
	# Merge the 2 new lists to get one list.		
	p1 = lessThan.head
	p2 = greaterThan.head.getNext()
	while(p1.getNext() != None):
		p1 = p1.getNext()		
	p1.setNext(p2)
	print "After partitioning:"
	lessThan.printLinkedList()
	return	
			


def main():
	# Create a single linked list with some values.
	myList = sll.SingleLinkedList()
	myList.insertNode(5)
	
	myList.insertNode(7)
	myList.insertNode(4)
	myList.insertNode(6)
	myList.insertNode(2)
	myList.insertNode(1)
	myList.insertNode(0)
	myList.insertNode(9)
	
	print "Before Partitioning:"
	myList.printLinkedList()
	partitionList(myList,5)

if __name__ == "__main__":
	main()





