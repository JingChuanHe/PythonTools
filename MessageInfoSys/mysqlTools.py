import pymysql
import hashlib
from io import BytesIO

#
# def dbClose(func):
#
# 	def wrapper(me_instance,*args,**kwargs):#
# 		print("dbClose")
# 		# print(kwargs)
# 		func(me_instance,args)
# 		print("8888888888888888888888888")
# 		# print(args)
# 		# print(funcSec)
# 	return wrapper
# # self.db.close()
class mysqlTools():

	def getImage(self):
		Id = 10
		sql = "SELECT IMAGE FROM employee WHERE Id = (%s)"
		cursor = self.db.cursor()

		try:
			# 执行sql语句
			cursor.execute(sql, Id)
			# t = cursor.fetchone()[0]
			with open('E:/PythonWorking/test/image3.JPG', 'wb') as file:
				file.write(cursor.fetchone()[0])
			cursor.close()
			# 提交到数据库执行
			# self.db.commit()
		except:
			# 如果发生错误则回滚
			self.db.rollback()
		self.db.close()


	# @dbClose
	def saveImage(self,image):
		print("saveImage")
		print(isinstance(image, bytes))

		# sql = "INSERT INTO employee (IMAGE) VALUES  (%s) WHERE Id = 2"

		# sql = "UPDATE employee SET IMAGE = '%s' WHERE Id = 9"
		sql = "update EMPLOYEE set IMAGE = (%s) where ID = 1 "
		cursor = self.db.cursor()
		try:
			# 执行sql语句
			# cursor.execute('UPDATE employee (TS) values (%s) WHERE Id = 2'%("ew"))
			cursor.execute(sql , [image] ) #%
			# 提交到数据库执行
			self.db.commit()
		except:
			# 如果发生错误则回滚
			self.db.rollback()
		self.db.close()

	def updateImage(self, image,Id):
		print("updateImage")
		# sql = "INSERT INTO employee (IMAGE) VALUES  (%s) WHERE Id = 2"

		# sql = "UPDATE employee SET IMAGE = '%s' WHERE Id = 9"
		sql = "update EMPLOYEE set IMAGE = (%s) where ID = (%s) "

		cursor = self.db.cursor()
		try:
			# 执行sql语句
			# cursor.execute('UPDATE employee (TS) values (%s) WHERE Id = 2'%("ew"))
			cursor.execute(sql, (image,Id))  # %
			# 提交到数据库执行
			self.db.commit()
		except:
			# 如果发生错误则回滚
			self.db.rollback()
			self.db.close()
	def insert_Info(self, image,Id):
		print("updateImage")
		# sql = "INSERT INTO employee (IMAGE) VALUES  (%s) WHERE Id = 2"

		# sql = "UPDATE employee SET IMAGE = '%s' WHERE Id = 9"
		sql = "update EMPLOYEE set IMAGE = (%s) where ID = (%s) "

		cursor = self.db.cursor()
		try:
			# 执行sql语句
			# cursor.execute('UPDATE employee (TS) values (%s) WHERE Id = 2'%("ew"))
			cursor.execute(sql, (image,4))  # %
			# 提交到数据库执行
			self.db.commit()
		except:
			# 如果发生错误则回滚
			self.db.rollback()
			self.db.close()
	def del_Info(self,Id):
		print("del_Info")

		sql = "delete from EMPLOYEE where ID = (%s) "

		cursor = self.db.cursor()
		try:
			# 执行sql语句
			# cursor.execute('UPDATE employee (TS) values (%s) WHERE Id = 2'%("ew"))
			cursor.execute(sql, (Id))  # %
			# 提交到数据库执行
			self.db.commit()
		except:
			# 如果发生错误则回滚
			self.db.rollback()
			self.db.close()

	def __init__(self,db_name):
		print("__init__SQLDB")
		# with pymysql.connect("localhost","root","root_jing","TESTDB") as db:
		# 	self.db = db
		self.db = pymysql.connect("localhost","root","root_jing",db_name)



#mysqlTools()