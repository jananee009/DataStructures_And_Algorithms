# Problem statement: Implement a Binary Search Tree. We assume that the tree will contain distinct data (key).
# Implement the following basic operations on the BST:
# 1. Insert, Search, Minimum, Maximum, Predecessor, Successor, Delete. 
# 2. Perform Traversals: BFS, DFS (Inorder, Pre ORder, Post Order).
# 3. Height of a tree  is a very important attribute of a BST.
# 4. The time complexity for basic operations is determined by the height of the tree O(h).

 

class Node: # Each node in the binary tree has 4 attributes namely data, leftChild, RightChild and Parent. Only the root node doesnt have a parent. 
	def __init__(self,_data,_left,_right,_parent):
		self.data = _data
		self.leftChild = _left
		self.rightChild = _right
		self.parent = _parent


	def setData(self,data):
		self.data = data
		return

	def getData(self):
		return self.data


	def setLeftChild(self,left):
		self.leftChild = left
		return


	def getLeftChild(self):
		return self.leftChild


	def setRightChild(self,right):
		self.rightChild = right
		return


	def getRightChild(self):
		return self.rightChild	

	def setParent(self,parent):
		self.parent = parent
		return


	def getParent(self):
		return self.parent	
		


class BinarySearchTree:
	def __init__(self,_Data,_Left,_Right,_Parent):
		self.count = 0
		self.root = Node(_Data,_Left,_Right,_Parent)		


	def insert(self,Data,x): # adds a new node to the binary tree. x is the root node of the tree to which we want to add a new node.
		newNode = Node(Data,None,None,None)
		self.current = x
		while(True):
			if (Data < self.current.getData()): # go left
				if(self.current.getLeftChild() == None):
					self.current.setLeftChild(newNode)
					newNode.setParent(self.current)
					break
				else:
					self.current = self.current.getLeftChild()
			elif (Data >= self.current.getData()): # add new node to the right.
				if(self.current.getRightChild() == None):
					self.current.setRightChild(newNode)
					newNode.setParent(self.current)
					break
				else:
					self.current = self.current.getRightChild()
		self.count = self.count + 1
		return


	# searches for a node in the tree. Returns a pointer to the node if it is found, otherwise it returns null.	
	# x is the root node of the tree  which we want to search.
	def search(self,Data,x): 
		self.current = x
		while(True):
			if(self.current.getData() == Data):
				return self.current
			if(Data<self.current.getData()): # search in left branch of the tree.
				self.current  = self.current.getLeftChild()
			elif(Data > self.current.getData()): # search in right branch of the tree.
				self.current = self.current.getRightChild()	
			if (self.current == None):
				return None


	# returns the lowest data found in the tree		
	# x is the root node of the tree whose minimum we want to find.	
	def findTreeMinimum(self,x):
		self.current = x
		while (self.current.getLeftChild() != None):
			self.current = self.current.getLeftChild()
		return self.current.getData()	


	# returns the highest data found in the tree	
	# x is the root node of the tree whose maximum we want to find.			
	def findTreeMaximum(self,x):
		self.current = x
		while (self.current.getRightChild() != None):
			self.current = self.current.getRightChild()
		return self.current.getData()	



	#  Successor of a node x is the node with the smallest key greater than x.key.
	# r  is the root node of the tree where we are going to search for predecessors.	
	def findSuccessor(self,Data,r):

		if (Data == self.findTreeMaximum(r)): 
			print "Cannot find successor of the tree maximum."
			return 

		# first find the node in the tree whose successor we want to find. We are interested in finding the successor of Data.
		x = self.search(Data,self.root) 	

		if ( x != None): # node is present in the tree

			if ( x.getRightChild() != None ): # x has a right child
				return self.findTreeMinimum(x.getRightChild())

			else: # x doesnt have a right child. x has a successor y, such that y is the lowest ancestor of x whose left child is also an ancestor of x.
			# Note: Every node is its own ancestor.
				y = x.getParent()
				while y != None and x == y.getRightChild():
					x = y
					y = y.getParent()

		return y.getData()			

					

		
	# Predecessor of a node x is the node with the largest key smaller than x.key	
	# r  is the root node of the tree where we are going to search for predecessors.
	def findPredecessor(self,Data,r):

		if (Data == self.findTreeMinimum(r)): 
			print "Cannot find predecessor of the tree minimum."
			return 

		# first find the node in the tree whose predecessor we want to find. We are interested in finding the successor of Data.
		x = self.search(Data,self.root) 	

		if ( x != None): # Node is present in the tree

			if ( x.getLeftChild() != None ): # x has a right child
				return self.findTreeMaximum(x.getLeftChild())

			else: # x doesnt have a left child. x has a predecessor y, such that y is the largest ancestor of x whose right child is also an ancestor of x.
			# Note: Every node is its own ancestor.
				y = x.getParent()
				while y != None and x == y.getLeftChild():
					x = y
					y = y.getParent()

		return y.getData()	



	def delete(self,Data,x):
		return	


	def inOrderTraversal(self,x):
		self.current = x
		while( x != None):
			self.inOrderTraversal(x.getLeftChild())
			print x.getData()
			self.inOrderTraversal(x.getRightChild())
		return


	def preOrderTraversal(self,x):
		return


	def postOrderTraversal(self,x):
		return		
				

	# Implements breadth first traversal	
	def breadthFirstSearch(self,x):
		childQ = []		
		childQ.append(x)
		while (len(childQ) > 0):
			node = childQ.pop(0)
			print node.getData()

			if (node.getLeftChild() != None):
				childQ.append(node.getLeftChild())
			if (node.getRightChild() != None):	
				childQ.append(node.getRightChild())
			

			



'''
def main():
	myBST = BinarySearchTree(15,None,None,None)

	# create binary search tree
	myBST.insert(6,myBST.root)
	myBST.insert(3,myBST.root)
	myBST.insert(7,myBST.root)
	myBST.insert(18,myBST.root)
	myBST.insert(2,myBST.root)
	myBST.insert(4,myBST.root)
	myBST.insert(13,myBST.root)
	myBST.insert(9,myBST.root)
	myBST.insert(17,myBST.root)
	myBST.insert(20,myBST.root)

	print "Tree Min: ",myBST.findTreeMinimum(myBST.root)
	print "Tree Max: ",myBST.findTreeMaximum(myBST.root)
	print "Successor: ", myBST.findSuccessor(13,myBST.root)
	print "Predecessor: ", myBST.findPredecessor(18,myBST.root)
	
	#print "In Order Traversal: ",myBST.inOrderTraversal(myBST.root)
	print "BFS Traversal: "
	myBST.breadthFirstSearch(myBST.root)





if __name__ == "__main__":
	main()	
'''

