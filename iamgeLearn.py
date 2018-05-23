from PIL import Image

import os, sys

path = "E:/PythonWorking/befor523/ImagePython/IMAGE"
class ImageLearn:

	def __init__(self):
		# self.zoomImage()
		# self.testAssert()

		'''对图片进行格式转换'''
		self.imageMethod()
	def zoomImage(self):
		im = Image.open('1.jpg')
		w,h = im.size
		print(w,h)
		im.thumbnail((w//2 ,h//2))
		# im.save('2.jpg','jpeg')

		im.save()
		print()
	def testAssert(self):
		i = 4
		assert i > 3,'i<3'

	def imageMethod(self):


		filelist = self.get_imlist()

		for infile in filelist:
			outfile = os.path.splitext(infile)[0] + ".jpeg"
			if infile != outfile:
				try:
					Image.open(infile).save(outfile)
				except IOError:
					print("cannot convert", infile)

	def get_imlist(self):
		""" 返回目录中所有JPG 图像的文件名列表"""
		return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]


ImageLearn()