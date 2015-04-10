__author__ = 'Niels'

import os, sys

class Folder():

	def __init__(self, file=__file__):
		self.__filepath = os.path.abspath(file)
		self.__path = self.parsePath()

	def getPath(self):
		return self.__path

	def parsePath(self):
		splitpath = self.__filepath.split("\\")
		splitpath.pop(len(splitpath)-1)
		stringpath = None
		for item in splitpath:
			if stringpath == None:
				stringpath = item
			else:
				stringpath += "/"+str(item)

		return stringpath

	def checkForFile(self, filename:str):
		""" returns True if the file exists """
		for item in os.listdir(self.getPath()):
			if filename in item:
				return True
		return False

	def getFiles(self):
		""" return list of files in the current folder """
		return os.listdir(self.getPath())
