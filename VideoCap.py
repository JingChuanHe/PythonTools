import os
from sys import stdin
from os import walk
from os.path import join

from tkinter import  *
import cv2

vc = cv2.VideoCapture('Test.avi')



def test():

	print('/*****/')
	print(os.getcwd())
	os.chdir('f:\\data\\a123')
	print(os.getcwd())
if __name__ == '__main__':
	test()