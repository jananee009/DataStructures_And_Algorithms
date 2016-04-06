
# Source: https://www.interviewcake.com/question/python/merge-sorted-arrays?utm_source=weekly_email
# We are given 2 sorted arrays containing numbers. We need to merge both arrays in to a single array of sorted numbers.
# Both lists can be of same  or different size. We will be creating a new sorted list that will contain elements from both lists.
# We will maintain a counter(index) for each input list.
# We compare one element from each list at a time. The smaller element is added to the new list. Increment the counter of the list to which the element belonged.
# Repeat this process until you reach the end of one list. 
# Add the remaining elements in the other list to the end of the new list. 
 


def mergeBothLists(myList,yourList):
	newList = []
	m = 0
	y = 0
	
	while(True):
		if myList[m] < yourList[y]: 
			newList.append(myList[m]) # as soon as we add an element to the newList, increment the counter of the list to which the element belonged.
			m += 1
		else:
			newList.append(yourList[y])
			y += 1
		
		if (m >= len(myList) and y >= len(yourList)): # both lists have been parsed.
			break

		elif ( (m >= len(myList) ) and y < len(yourList)): # first list is parsed and the second one has some unparsed elements.
			newList.extend(yourList[y:])
			break

		elif ( (m < len(myList) ) and y >= len(yourList)): # second list is parsed and the firt one has some unparsed elements.
			newList.extend(myList[m:])	
			break

		else:
			continue	
	
	print "List1: ",myList
	print "List2: ",yourList
	print "Merged Sorted List: ",newList			

	return 		



		
def main():
	mergeBothLists([3, 4, 6, 10 ], [1, 5, 8, 12, 14, 19])



if __name__ == "__main__":
	main()	
	


