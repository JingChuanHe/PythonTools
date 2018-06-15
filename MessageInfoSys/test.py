# -*- coding=utf-8 -*-
import pymysql
import sys

# 读取图片文件

# fp = open("test.jpg",'rb',encoding='utf-8')
# fp = open("E:/PythonWorking/befor523/AutomateTheBoringStuffWithPython/mv/122600094962.JPG", 'rb')
# img = fp.read()
# fp.close()
# 创建连接
# conn = pymysql.connect(host='localhost',
# 					   port=3306,
# 					   user='root',
# 					   passwd='root_jing',
# 					   db='python_operation_01',
# 					   charset='utf8',
# 					   use_unicode=True, )
conn = pymysql.connect("localhost","root","root_jing",'TESTDB')
# 创建游标
cursor = conn.cursor()

with open('E:/PythonWorking/befor523/AutomateTheBoringStuffWithPython/mv1/122600094811.JPG', 'rb') as fp:
	data = fp.read()
cursor.execute("update EMPLOYEE set IMAGE = (%s) where ID = 3 ", [data])
# cursor.execute("insert into EMPLOYEE (IMAGE) values (%s)",data)
# cursor.execute("insert into EMPLOYEE  values ('11','JING','CHUAN',21,'F',91110,%s,'OL')",data)

# cursor.execute("UPDATE EMPLOYEE SET IMAGE = (%s) WHERE Id = 1" % (data))

# 提交，不然无法保存新建或者修改的数据
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()