__author__ = 'Niels'

import folderStructure.folder as folder
from json import *
from Database import dataBase, Table
from pymongo.mongo_client import MongoClient



class DataManager():

	def __init__(self, address):
		self.dbClient = MongoClient(address)
		self.db = self.dbClient.mydb
		self.tables = self.getTables()



	def getTables(self)->dict:
		return Table.Table(self.db)


	def getData(self, table=None):
		if table:
			return self.tables[table]
		else:
			return self.tables




