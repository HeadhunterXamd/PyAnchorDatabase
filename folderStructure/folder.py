__author__ = 'Niels'

import os, sys

class Folder():

	def __init__(self, file):
		self.__filepath = os.path.abspath(file)
		self.__path = self.parsePath()

	def getPath(self):
		return self.__path

	def parsePath(self):
		p = self.__filepath.split("\\")
		p.pop(len(p)-1)
		s = None
		for item in p:
			if s == None:
				s = item
			else:
				s += "/"+str(item)

		return s

	def checkForFile(self, filename:str):
		""" returns True if the file exists """
		for item in os.listdir(self.getPath()):
			if filename in item:
				return True
		return False

	def getFiles(self):
		""" return list of files in the current folder """
		return os.listdir(self.getPath())