__author__ = 'Niels'

import folderStructure.folder as folder
from json import *
import Database.Table as table

class DataManager():

	def __init__(self):
		from pymongo.mongo_client import MongoClient as mc
		self.folder = folder.Folder(__file__)
		self.dbClient = mc('mongodb://localhost:27017/')
		self.db = self.dbClient.mydb
		self.tables = self.getTables()



	def getTables(self)->dict:
		return table.Table(self.db)


	def getData(self, table=None):
		if table:
			return self.tables[table]
		else:
			return self.tables




