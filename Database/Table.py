__author__ = 'Niels'
from json import *

class Table():

	def __init__(self, file):
		self.data = dict(self.parseTablefile(file))
		self.keys = self.data.keys()
		self.values = self.data.values()

	def __str__(self):
		string = "key -> value \n"
		for item in self.data.keys():
			string += item +" -> "+str(self.data[item])+"\n"
		return string

	def __repr__(self):
		return str(self.data)

	def parseTablefile(self, file):
		return load(open(file,"r"))

#
# w = Table("test.table")
#
# print(w)