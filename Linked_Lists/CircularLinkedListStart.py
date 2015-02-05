# Given a circular linked list, implement an method that returns the node at the beginning of the loop
# Approach: Have 2 pointers Fast and Slow to iterate through the linked list.
# Slow pointer moves one node at a time. Fast pointer moves 2 nodes at a time. 
# When slow pointer is 1 node in to the list, fast pointer is already 2 nodes in to the list.
# if both pointers meet on the same node, we know there is a loop in the linked list. 
# Once loop is detected, move the slow pointer back to the head. Keep the fast pointer where it is. Move both pointers one node at a time.
# The node where they coolide is the starting node of the loop. 


import SinglyLinkedList as sll



def detectLoopHead(linkedlist):
	slowPtr = linkedlist.head
	fastPtr = linkedlist.head
	# detect circular loop in the linked list.
	while(slowPtr != None and fastPtr != None):
		slowPtr = slowPtr.getNext()
		fastPtr = fastPtr.getNext().getNext()
		if(slowPtr == fastPtr):
			print "Ciruclar Loop Detected."
			break
	# move slow pointer to the start of the loop.	
	slowPtr = linkedlist.head
	while(slowPtr != fastPtr):
		slowPtr = slowPtr.getNext()
		fastPtr = fastPtr.getNext()
	print "Circular Loop in the linked list begins at: ",slowPtr.getData()	
	return


def main():
	# Code to create a circular linked list with loop starting  at node 300.

	# Create a singly linked list first.
	myList = sll.SingleLinkedList()

	myList.insertNode(100)
	myList.insertNode(200)
	myList.insertNode(300)
	myList.insertNode(400)
	myList.insertNode(500)
	myList.insertNode(600)
	myList.insertNode(700)


	# Get to the last node in the singly linked list.
	curr1 = myList.head
	while(curr1.getNext() != None):
		curr1 = curr1.getNext()

	# Get to node with value 300. 
	curr2 = myList.head
	while(curr2.getNext() != None and curr2.getData() != 300):
		curr2 = curr2.getNext()
		print curr2.getData()

	# Connect the last node of the list to node with value 300.	
	curr1.setNext(curr2)	

	detectLoopHead(myList)



if __name__ == "__main__":
	main()