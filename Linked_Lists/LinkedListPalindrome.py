# Implement a function to check if a linked list is a palindrome.
# Approach : Access the linked list in reverse and compare it with the linked list. If it is the same, then we have a palindrome.




import SinglyLinkedList as sll



def checkPalindrome(list):
	curr = list.head
	tempList = []
	while(curr.getNext() != None):
		curr = curr.getNext()
		tempList.append(curr.getData())
	origList = tempList[:]
	tempList.reverse()
	if(tempList == origList):
		print "Linkedlist is a palindrome."
	else:
		print "Linkedlist is not a palindrome."	
	return	


def main():
	# Code to create a circular linked list with loop starting  at node 300.

	# Create a singly linked list first.
	myList = sll.SingleLinkedList()

	myList.insertNode(100)
	myList.insertNode(200)
	myList.insertNode(300)
	myList.insertNode(400)
	myList.insertNode(300)
	#myList.insertNode(200)
	#myList.insertNode(100)

	myList.printLinkedList()
	checkPalindrome(myList)




if __name__ == "__main__":
	main()