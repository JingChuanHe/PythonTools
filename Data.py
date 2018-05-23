from tkinter import *
import xlrd
import xlwt
import os
class excelT:
	def __init__(self):
		window = Tk(className = "处理数据")
		window.geometry('190x90+150+150')
		lable = Label(window,text = "Filename")


		self.msg = StringVar()
		self.msg1 = StringVar()
		entryName = Entry(window,textvariable= self.msg)
		entryName1 = Entry(window, textvariable=self.msg1)

		readButton = Button(window, text="Read", fg="red", command=self.read_excel)
		writeButton = Button(window, text="Write", fg="red", command=self.save_excel)


		lable.grid(row=1, column=1)
		entryName.grid(row=2, column=1)
		entryName1.grid(row = 3,column=1)
		readButton.grid(row=2, column=2)
		writeButton.grid(row = 3,column = 2)

		window.mainloop()


	def clickMe(self):
		print("Clicke Me ",self.msg.get())
		self.read_excel()

	def read_excel(self):
		print("Come", self.msg.get())
		excelName = self.msg.get() + ".xlsx"
		# 打开文件
		file_Name = 'F:\data' + '\\' + excelName
		workbook = xlrd.open_workbook(file_Name)
		sheet2 = workbook.sheet_by_index(0)
		cols = sheet2.col_values(0)  # 获取第一列内容
		print("/****************Wright Excel*******************/")
		m = 0
		self.listMax = []
		for i in range(21, len(cols)):
			if int(cols[i]) == m:
				m = m + 1
				list0 = sheet2.row_values(i)
				self.listMax.append(list0)
				print(self.listMax)
				print("/****************INT*******************/")


	def save_excel(self):
		print(os.getcwd())
		os.chdir('f:\\data\\NewData')
		print(os.getcwd())
		print("Come",self.msg1.get(),self.listMax)
		excelName = self.msg1.get() + ".xls"
		f = xlwt.Workbook()
		sheet2 = f.add_sheet('sheet1', cell_overwrite_ok=True)
		row0 = ['时间s', '力kN', '变形mm', '位移mm', '扩展', '应力MPa', '应变%']

		for i in range(0, len(row0)):
			sheet2.write(0, i, row0[i])

		for j in range(0, len(self.listMax)):
			data1 = self.listMax[j]
			for i in range(0, len(row0)):
				sheet2.write(j + 1, i, data1[i])
		f.save(excelName)  # 保存文件


excelT()





