# Write a program to remove duplicates from an unsorted linked list.
# Follow up question: How would you solve this problem if a temporary buffer is not allowed.
# We will use a doubly linked list. 
# Approach:  With temporary buffer: Use a list. As you iterate through the list, check if the element in the node is already present in the list. 
# If the element is not present, add it to the list. If it is present, then the node is a duplicate node. Remove the duplicate node. 
# Approach: Without temporary buffer: Use 2 iterators. Both iterators will visit each node in the list. 
# While the first iterator points to one node, the 2nd iterator will start iterating from the next node and visit each subsequent node till it reaches the end of the list. 
# As the 2nd iterator visits each node, it compares the data with the data present in the node pointed at by the first iterator. In case the data matches,
# a duplicate node has been found by the 2nd iterator and it will be removed. 

import DoublyLinkedList as dll


def removeDuplicates(linkedlist):
	temp = [] # This list will store the unique elements in the linked list.
	print "Size of the linked list BEFORE removing duplicates: ", linkedlist.getSize()
	curr = linkedlist.head
	while(curr.getNext() != None):
		curr = curr.getNext()
		if (curr.getData() in temp):
			# if the data in the current node exists in the list, it is a duplicate. Hence, remove the node from the list.
			if(curr.getNext() != None): 
			# if the duplicate node IS NOT the last node in the linked list.
				curr.getNext().setPrev(curr.getPrev())
				curr.getPrev().setNext(curr.getNext())
			else: 
				# if the duplicate node is the last node in the list, set the next pointer of its previous node to None. 
				curr.getPrev().setNext(None)
		else:
			# add the data in the node to the list.
			temp.append(curr.getData())
	print "Size of the linked list AFTER removing duplicates: ", linkedlist.getSize()		
	return			

	
def removeDuplicatesNoAdditionalMemory(linkedlist):
	print "Size of the linked list BEFORE removing duplicates: ", linkedlist.getSize()
	curr = linkedlist.head
	while(curr.getNext() != None):
		curr = curr.getNext()
		runner = curr
		while(runner.getNext() != None):
			runner = runner.getNext()
			if(curr.getData() == runner.getData()):
				# Duplicate node found. Remove the node.
				if(runner.getNext() != None): 
					# if the duplicate node IS NOT the last node in the linked list.
					runner.getNext().setPrev(runner.getPrev())
					runner.getPrev().setNext(runner.getNext())
				else: 
					# if the duplicate node is the last node in the list, set the next pointer of its previous node to None. 
					runner.getPrev().setNext(None)	
	print "Size of the linked list BEFORE removing duplicates: ", linkedlist.getSize()												
	return				









def main():
	# Create a doubly linked list with duplicates
	myList = dll.DoubleLinkedList()

	myList.insertNode(100)
	myList.insertNode(200)
	myList.insertNode(300)
	myList.insertNode(400)
	myList.insertNode(300)
	myList.insertNode(200)

	print "Before removing duplicates: "
	myList.printLinkedList()
	#removeDuplicates(myList)
	removeDuplicatesNoAdditionalMemory(myList)	

	print "After removing duplicates: "
	myList.printLinkedList()




if __name__ == "__main__":
	main()