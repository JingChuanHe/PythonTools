# -*- coding: utf-8 -*-
import xlrd

import xlwt

def read_excel():
	# 打开文件
	workbook = xlrd.open_workbook(r'F:\data\00.xlsx')
	sheet2 = workbook.sheet_by_index(0)
	cols = sheet2.col_values(0)  # 获取第一列内容
	print("/****************Wright Excel*******************/")
	m = 0
	listMax = []
	for i in range(21,len(cols)):
		if int (cols[i]) == m:
			m = m + 1
			list0 = sheet2.row_values(i)
			listMax.append(list0)
			print(listMax)
			print("/****************INT*******************/")
	save_excel(listMax)

def save_excel(data0 ):
	f = xlwt.Workbook()
	sheet2 = f.add_sheet('sheet1', cell_overwrite_ok=True)
	row0 = ['时间s', '力kN', '变形mm', '位移mm', '扩展','应力MPa','应变%']

	for i in range(0, len(row0)):
		sheet2.write(0, i, row0[i])

	for j in range(0,len(data0)):
		data1 = data0[j]
		for i in range(0, len(row0)):
			sheet2.write(j+1, i, data1[i])
	f.save('demo13.xls')  # 保存文件


if __name__ == '__main__':
	read_excel()
