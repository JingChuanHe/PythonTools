from MessageInfoSys.mysqlTools import mysqlTools
from PIL import Image

class infoNet():

	def __init__(self):

		self.sqlTools = mysqlTools('TESTDB')
		# with open('E:/PythonWorking/befor523/AutomateTheBoringStuffWithPython/mv1/122600095003.JPG','rb') as imageNet:
		# 	imageStrom = imageNet.read()
		# 	print(type(imageStrom))
		# 	print(imageNet.read())
		# 	with open('E:/PythonWorking/test/image.JPG', 'wb') as file:
		# 		byteCount = file.write(imageStrom)
		# 		print(byteCount)







		# 	# self.sqlTools.cursor.fetcsaveImage(imageStrom)
		# 	self.sqlTools.updateImage(imageStrom,9)
		# 	# self.sqlTools.del_Info(11)
		self.sqlTools.getImage()


infoNet()