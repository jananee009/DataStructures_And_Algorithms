# Write a recursive function for generating all permutations of an input string. Return them as a set.
# Source: https://www.interviewcake.com/question/python/recursive-string-permutations
# Approach: Suppose we have a string "abcd" for which we want to generate all permutations. 
# Maintain a list to store all permutatations. (Say, it is called perm).
# Process each character in the string one by one:
# For letter a:
# Since it is the very first character, add it to the empty list perm . Hence, perm = [a]
# For letter b: Take the first item from perm ( i.e. a). We want to find all possbile "seats" for the letter b around a. 
# For any character, imagine that there is one space to the left of it and one to the right of it. 
# Something like this: _a_. i.e. there are 2 seats available for b to sit. We will put "b" in each of these seats. 
# Thus we have "ba" and "ab". Save these to perm. Now, perm = ["ab", "ba"].
# For letter c: Take the first item from perm (i.e. "ab"). For the letter c to sit with "ab", the possible seats are: first seat, one seat between a and b and one at the end. 
# i.e. _a_b_. Thus we have "cab", "acb", "abc". 
# Take the next item from perm (i.e. "ba"). For the letter c to sit with "ba", the following seats are available: _b_a_. Thus we have "cba", "bca", "bac".
# Save all of these to perm. Now, perm = [ "cab", "acb", "abc", "cba", "bca", "bac"].
# For letter d: Repeat the process as above. 






		

def permutations(inputString): # without using recursion
	perm = []
	temp = []
	for character in inputString:
		if perm: # check if perm is empty
			# place the character in available seats around eachString.
			temp = [ eachString[:index] + character + eachString[index:] for eachString in perm for index in range(len(eachString)+1) ]					
		else: # perm is empty. So, this means we are processing the first character of the inputString. 
			temp.append(character)

		perm = temp		
	return perm	


						


		
def main():
	givenString = "abcd"
	print (permutations(givenString))



if __name__ == "__main__":
	main()	
	


