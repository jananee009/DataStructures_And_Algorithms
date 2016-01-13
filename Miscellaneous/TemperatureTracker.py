# Problem 7: Temperature Tracker
# Source: https://www.interviewcake.com/question/python/temperature-tracker
# You decide to test if your oddly-mathematical heating company is fulfilling its All-Time Max, Min, Mean and Mode Temperature Guarantee

class TempTracker:
	def __init__(self):

		self.maxTemp = -1 # for tracking max temperature
		self.minTemp = 111 # for tracking min temperature
		
		self.countTemperatures = {} # dictionary to store each recorded temperature and the number of times it has been recorded. 
		
		# for computing mean of temperatures
		self.sumOfTemperatures = 0
		self.numberOfTemperatures = 0
		


	# method to record a new temperature	
	def insert(self,newTemperature):	
		if 0 <= newTemperature <= 110:

			# for computing mean temperature
			self.sumOfTemperatures = self.sumOfTemperatures + newTemperature
			self.numberOfTemperatures += 1

			# for max temperature
			if newTemperature > self.maxTemp:
				self.maxTemp = newTemperature
			
			# for min temperature
			if 	newTemperature < self.minTemp:
				self.minTemp = newTemperature

			# for mode	
			if newTemperature in self.countTemperatures.keys():
				self.countTemperatures[newTemperature] += 1					
			else:
				self.countTemperatures[newTemperature] = 1			
		else:
			print "Invalid temperature."
		return
		
	

	# computes the mean of all recorded temperatures.			
	def get_mean(self):
		return self.sumOfTemperatures / float(self.numberOfTemperatures)


	def get_max(self):
		return self.maxTemp


	
	def get_min(self):	
		return self.minTemp


	def get_mode(self):		
		maxValue = max(self.countTemperatures.values())
		modeTemp = [k for k,v in self.countTemperatures.iteritems() if v == maxValue ]	
		return modeTemp	

			


	

		
def main():
	mytempTracker = TempTracker()
	mytempTracker.insert(10)
	mytempTracker.insert(20)
	mytempTracker.insert(20)
	mytempTracker.insert(30)
	print "Mean Temp: ",mytempTracker.get_mean()
	print "Min Temp: ",mytempTracker.get_min()
	print "Max Temp: ",mytempTracker.get_max()
	print "Mode Temp: ",mytempTracker.get_mode() 




if __name__ == "__main__":
	main()	
	


