# Write a function to find the rectangular intersection of two given love rectangles. 
# Question Source: https://www.interviewcake.com/question/rectangular-love
		

class Rectangle:
	def __init__(self,BL_Coordinates,height,width):
		# BL_coordinates is a tuple (x,y)
		self.BL = BL_Coordinates 		# BL = Bottom Left
		self.h = height
		self.w = width
		self.BR = (BL_Coordinates[0]+width,BL_Coordinates[1]) # BR == Bottom Right
		self.TL = (BL_Coordinates[0],BL_Coordinates[1]+height) # TL == Top Left
		self.TR = (BL_Coordinates[0]+width,BL_Coordinates[1]+height) #TR == Top Right

			
	def findWhichCornersInside(self,rect1,rect2): # find which corner(s) of the second rectangle  are inside the first one.

		BL_inside = False
		BR_inside = False
		TL_inside = False
		TR_inside = False


		# Check if BL corner is inside
		if ((rect1.BL[0]  <  rect2.BL[0] < rect1.BR[0]) and ( rect1.BL[1] < rect2.BL[1] < rect1.TL[1])):
			BL_inside = True


		# Check if BR corner is inside
		if(rect1.BL[0]  <  rect2.BR[0] < rect1.BR[0]) and (rect1.BL[1]  <  rect2.BR[1] < rect1.TL[1]):
			BR_inside = True


		# Check if TL corner is inside
		if(rect1.BL[0]  <  rect2.TL[0] < rect1.BR[0]) and (rect1.BR[1]  <  rect2.TL[1] < rect1.TR[1]):	
			TL_inside = True


		# Check if TR corner is inside
		if(rect1.BL[0]  <  rect2.TR[0] < rect1.BR[0]) and (rect1.BL[1]  <  rect2.TR[1] < rect1.TL[1]):	
			TR_inside = True

		# All 4 corners are inside	
		if (BL_inside and BR_inside and TL_inside and TR_inside):
			print "All 4 corners of the 2nd rectangle are inside the first."
			return ["BL","BR","TL","TR"]
		
		# Both BL and BR are inside
		elif(BL_inside and BR_inside):
			print "Bottom Left and Bottom Right corners are inside."
			return ["BL","BR"]
		

		# Both BL and TL are inside	
		elif(BL_inside and TL_inside):	
			print "Bottom Left and Top Left corners are inside."
			return ["BL","TL"]

		# Both TL and TR are inside
		elif(TL_inside and TR_inside):	
			print "Top Left and Top Right corners are inside."
			return ["TL","TR"]

		# Both BR and TR are inside
		elif(BR_inside and TR_inside):
			print "Bottom Right and Top Right Corners are inside."	
			return ["BR","TR"]	

		#Only BL is inside
		elif(BL_inside):
			print "Only Bottom left is inside."
			return ["BL"]

		#Only BR is inside
		elif(BR_inside):
			print "Only Bottom Right is inside."
			return ["BR"]

		#Only TL is inside
		elif(TL_inside):
			print "Only Top left is inside."
			return ["TL"]

		#Only TR is inside
		elif(TR_inside):
			print "Only Top Right is inside."
			return ["TR"]

		else:
			print "None of the corners of the 2nd rectangle are inside the first."	
			return []



	def findOverlap(self,cornersList,rect1,rect2): 
	# This function computes how much height and width of the 2nd rectangle lies inside the first one.	
		if (len(cornersList) < 1):
			print "There is no overlap between the 2 rectangles."
			return []

		if (len(cornersList)==1): # only one corner is inside.
			if (cornersList[0] == "BL"):
				overLap_h = rect1.TL[1] - rect2.BL[1]
				overLap_w = rect1.TR[0] - rect2.BL[0]
				
		
			elif (cornersList[0] == "BR"):
				overLap_h = rect1.TL[1] - rect2.BR[1]
				overLap_w = rect2.BR[0] - rect1.BL[0]
				

			elif (cornersList[0] == "TL"):
				overLap_h = rect2.TL[1] - rect1.BL[1]
				overLap_w = rect1.TR[0] - rect2.TL[0]
				

			elif (cornersList[0] == "TR"):
				overLap_h = rect2.TR[1] - rect1.BL[1]
				overLap_w = rect2.TR[0] - rect1.BL[0]

		elif (len(cornersList) == 2): # 2 corners are inside	
			if (cornersList == ["BL","BR"]):
				overLap_h = rect1.TL[1] - rect2.BL[1]
				overLap_w = rect2.BR[0] - rect2.BL[0]

			elif (cornersList == ["BL","TL"]):
				overLap_h = rect2.TL[1] - rect2.BL[1]
				overLap_w = rect1.BR[0] - rect2.BL[0]

			elif (cornersList == ["TL","TR"]):
				overLap_h = rect2.TL[1] - rect1.BL[1]
				overLap_w = rect2.TR[0] - rect2.TL[0]

			elif (cornersList == ["BR","TR"]):
				overLap_h = rect2.TR[1] - rect2.BR[1]
				overLap_w = rect2.BR[0] - rect1.BL[0]	

		elif (len(cornersList) == 4):
				print "2nd rectangle is completely inside first one."
				overLap_h = rect2.TL[1] - rect2.BL[1]
				overLap_w = rect2.BR[0] - rect2.BL[0]

		return [overLap_h,overLap_w]	



def main():
	myRect1 = Rectangle((1,5),4,7)
	#myRect2 = Rectangle((8,9),2,4) #test case for 2nd rectangle is completely outside first one. i.e. there is no intersection
	#myRect2 = Rectangle((2,6),2,4) #test case for 2nd rectangle is completely inside first one. 
	# myRect2 = Rectangle((7,8),5,4) #test case for only bottom left inside 
	#myRect2 = Rectangle((-2,0),6,5) #test case for only top right inside 
	#myRect2 = Rectangle((-2,6),6,5) #test case for only bottom right inside 
	#myRect2 = Rectangle((6,0),6,5) #test case for only top left inside 

	#myRect2 = Rectangle((3,8),5,4) #test case for only bottom left and bottom right inside 
	#myRect2 = Rectangle((7,6),2,5) #test case for only top left and top right inside 
	#myRect2 = Rectangle((-2,6),2,5) #test case for only bottom right left and top right inside

	dummyRect = Rectangle((0,0),0,0) # This object is used only to call the class methods
	insideCorners = dummyRect.findWhichCornersInside(myRect1,myRect2)
	overLap = dummyRect.findOverlap(insideCorners,myRect1,myRect2)
	print "Result: "
	print "Bottom left corner of 2nd rectanlge: ", myRect2.BL
	print "Overlap height and width: ",overLap



if __name__ == "__main__":
	main()




	