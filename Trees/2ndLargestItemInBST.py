# Write a function to find the 2nd largest element in a binary search tree. 
# Approach: 1. Given a BST, if the tree has right subtree then the largest element is the right most element of the right sub tree. 
# a) If the largest element node is a leaf node, then the 2nd largest element of the tree is its parent. 
# b) If the largest element node has a left child (but not a right one), then the left child element is the 2nd largest element of the tree. 
# 2. If the BST doesnt have a right sub tree and has only a left sub tree:
# a) Then the 2nd largest element in the wholte tree is the largest element in the left sub tree. 

import BinarySearchTree as bst

# accepts root node for a tree and finds the largest element in the tree.
def findTreeMaximum(inputNode): 
	currentNode = inputNode

	while currentNode.getRightChild() != None:
		currentNode = currentNode.getRightChild()
	return currentNode.getData()


def find2ndLargestElement(rootNode):
	currentNode = rootNode

	# if BST has right sub tree, then the 2nd largest item will be found in the right sub tree.
	if (currentNode.getRightChild() != None):

		while(currentNode.getRightChild() != None): # get the right most node (highest element of the tree)
			currentNode = currentNode.getRightChild()
		

		if 	currentNode.getLeftChild() != None: # if the largest node has a left child, then the largest element in the left sub tree is the 2nd largest item in the whole tree.
			currentNode = currentNode.getLeftChild()
			
			print "Second largest item in the tree: ", findTreeMaximum(currentNode)
			return

		else: # largest node doesnt have a left sub tree. 
			print  "Second largest item in the tree: ", currentNode.getParent().getData()
			return

	elif (currentNode.getLeftChild() != None): # tree doesnt have a right sub tree. It has only left sub tree.

		currentNode = currentNode.getLeftChild()
		print  "Second largest item in the tree: ", findTreeMaximum(currentNode) # the largest element in the left sub tree is the 2nd largest item in the whole tree.
		return

	else:
		print "Tree has only root node."
		return	





def main():
	myBST = bst.BinarySearchTree(137,None,None,None) # Root Node

	myBST.insert(42,myBST.root)
	myBST.insert(99,myBST.root)
	
	myBST.insert(23,myBST.root)
	myBST.insert(14,myBST.root)
	myBST.insert(19,myBST.root)
	myBST.insert(12,myBST.root)
	myBST.insert(76,myBST.root)
	myBST.insert(54,myBST.root)
	myBST.insert(72,myBST.root)
	myBST.insert(67,myBST.root)
	
	find2ndLargestElement(myBST.root)




	

if __name__ == "__main__":
	main()


	