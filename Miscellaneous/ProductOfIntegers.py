# Problem Source: https://www.interviewcake.com/question/product-of-other-numbers
# You have an array of integers, and for each index you want to find the product of every integer except the integer at that index.
# Write a function get_products_of_all_ints_except_at_index() that takes an array of integers and returns an array of the products.
# Example: Given
# [1,7,3,4]
# Output
# [84,12,28,21]
# by calculating
# [7*3*4, 1*3*4, 1*7*4, 1*7*3]



# this method uses a brute force approach to solve the problem.
# Runtime Complexity: o(n^2)
def get_products_of_all_ints_except_at_index():
	givenList = input("Enter a list of integers: ") # list of numbers input by user.
	# for e.g. enter input as: [3, 1, 2, 5, 6, 4]
	if (len(givenList)) == 0:
		print  "You have entered an empty list."
		return
	productList = [] # this list will have the product of numbers, the required result.
	# We know that the productList will have the same number of elements as that of the givenList. 
	for i in range(0,len(givenList)):  # i stands for ith product in the  list of product of numbers. 
		prod = 1
		for j in range(0,len(givenList)): # j is the index of the input list of numbers. 
			if (i == j): # e.g. if the 1st product is being calculated, and if we are on the 1st number in the input list, dont do anything. Just go to the next number. 
				pass # do nothing
			else: # otherwise, Use the number to calculate the product
				prod = prod*givenList[j]
		productList.append(prod) # add the calculated product to the product list.
	print productList 	
	return			
	

def main():
	get_products_of_all_ints_except_at_index()
	
	


if __name__ == "__main__":
	main()


