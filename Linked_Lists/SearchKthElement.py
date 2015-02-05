# Write a program to find the kth to the last element of a singly linked list.
# Approach: If you know the size of the linked list, then this is a very easy problem to solve. Assume that the size of the list is unknown.
# We use an iterative approach. We use 2 pointers: curr and runner. We place the 2 pointers such that they are k nodes apart. 
# If curr points to the first node, then runner points to kth node from curr. We move both pointers such that they are always k nodes apart. 
# When the runner hits the last node, curr will point to the kth node from the last.

import SinglyLinkedList as sll

def searchKthElementFromLast(linkedlist,k):
	if(k<=0):
		print "Invalid k value."
		return
	curr = linkedlist.head.getNext()
	runner = linkedlist.head.getNext()
	for i in range(1,k):
		if(runner.getNext() != None):
			runner = runner.getNext()
		else: # Error condition
			print "Invalid k value. Value of k larger than size of the linked list"
			return
	while(runner.getNext() != None):
		curr = curr.getNext()
		runner = runner.getNext()
		print runner.getData()
	print  "The ", k, "th to last element in the list is: ",curr.getData()
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
	user_input = input("Enter a whole number: ")
	searchKthElementFromLast(myList,user_input)



if __name__ == "__main__":
	main()