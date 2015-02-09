__author__ = 'Niels'
from json import *
from pymongo import MongoClient

class Table(dict):

	def __init__(self, db):
		self.db = db
		self.data = self.parseTablefile()
		self.keys = self.data.keys()
		self.values = self.data.values()



	def __str__(self):
		string = "key -> value \n"
		for item in self.data.keys():
			string += item +" -> "+str(self.data[item])+"\n"
		return string

	def __repr__(self):
		return str(self.data)

	def parseTablefile(self):
		return self.db.data.find_one()

	def getItem(self, *args):
		for arg in args:
			if arg in self.keys:
				return self.data[arg]

#
# w = Table("test.table")
#
# print(w)