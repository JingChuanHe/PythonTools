import numpy as np
import re
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
class numpyLearn:
	def __init__(self):
		self.test()
		#self.binomial()
		# self.normalDistribute()
	def test(self):
		print("222")
		data_x = np.loadtxt("ee.txt",usecols=(1,),unpack=True)
		data_y = np.loadtxt("ee.txt",usecols=(2,),unpack=True)
		x = np.array(data_x)
		print(data_x,x)
	def binomial(self):
		print("ddd")
		cash = np.zeros(10000)
		cash[0] = 1000
		outcome = np.random.binomial(9,0.5,size=len(cash))
		for i in range(1,len(cash)):
			if outcome[i] < 5:
				cash[i] = cash[i-1] - 1
			elif outcome[i] < 10:
				cash[i] = cash[i-1] +1
			else:
				raise AssertionError("Unexcept outcome "+outcome)
		print(outcome.min(),outcome.max())
		plot(np.arange(len(cash)),cash)
		show()

		print(outcome)
	def normalDistribute(self):
		print("05")
		N = 10000
		normal_values = np.random.normal(size=N)
		dummy, bins, dummy = plt.hist(np.array(normal_values), np.sqrt(N), normed=True, lw=1)
		sigma = 1
		mu = 0
		plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-(bins - mu)**2 / (2 * sigma**2)), lw=2)
		plt.show()
numpyLearn()