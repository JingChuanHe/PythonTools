from tkinter import *

master = Tk()

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()

def testCMD(content):
	return content.isdigit()

e1 = Entry(master,textvariable = v1,validate="key",\
		   validatecommand=(testCMD,'%P')).grid(row = 0,column = 0)
Label(master,text = "+").grid(row = 0,column = 1)

e1 = Entry(master,textvariable = v2,validate="key",\
		   validatecommand=(testCMD,'%P')).grid(row = 0,column = 2)
Label(master,text = "=").grid(row = 0,column = 3)
e1 = Entry(master,textvariable = v3,validate="key",\
		   validatecommand=(testCMD,'%P')).grid(row = 0,column = 4)
def calc():
	result = int(v1.get())+int(v2.get())
	v3.set(str(result))
	print(111)

Button(master,text = "EQ",command = calc).grid(row= 1,column = 2)

mainloop()