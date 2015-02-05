# Problem: You have 2 numbers represented by a linked list, where each node contains a single digit. The digits are stores in reverse order, 
# such that the 1s digit is at the head of the list. Write a function that adds the 2 numbers and returns the result as a linked list.
# EXAMPLE: Input: (7->1->6) + (5->9->2). That is 617+295.
# Output: 2->1->9. i.e. 912.

import SinglyLinkedList as sll


def AddNumbersInLists(linkedlist1,linkedlist2):
	# use 2 pointers to iterate through 2 numbers i.e. 2 linked lists.
	p1 = linkedlist1.head
	p2 = linkedlist2.head

	resultList = sll.SingleLinkedList() # linked list contains the result of addition
	r1 = resultList.head
	temp = 0 # to store carry over digits during addition.
	while(p1.getNext() != None and p2.getNext() != None):
		p1 = p1.getNext()
		p2 = p2.getNext()
		sum = p1.getData() + p2.getData() + temp
		resultList.insertNode((sum%10)) # extract the units digit of the sum and insert it to the result linked list.
		if (sum/10 != 0): # extract the tens digit and store it in temp, to be used for carry over addition.
			temp = sum/10
		else:
			temp = 0	
	if (temp > 0): #If the result of adding two 3-digit numbers gives a 4-digit number, this if loop inserts the 4 digit in to the result linked list.
		resultList.insertNode(temp)		
	print "After Adding, result:"
	resultList.printLinkedList()		
	return	
			


def main():
	# Create a single linked list with some values.
	myList1 = sll.SingleLinkedList()
	myList2 = sll.SingleLinkedList()
	myList1.insertNode(7)
	
	myList1.insertNode(8)
	myList1.insertNode(9)
	myList2.insertNode(6)
	myList2.insertNode(5)
	myList2.insertNode(7)
	
	print "Before Adding,2 numbers:"
	myList1.printLinkedList()
	myList2.printLinkedList()
	AddNumbersInLists(myList1,myList2)
	

if __name__ == "__main__":
	main()





