__author__ = 'Niels'

import folderStructure.folder as folder
from json import *
import Database.Table as table


class DataManager():

	def __init__(self):
		self.folder = folder.Folder(__file__)
		self.tables = self.getTables()


	def getTables(self)->dict:
		retDict = {}
		files = self.folder.getFiles()
		for file in files:
			if ".py" not in file:
				if "__" not in file:
					key = file[:file.index(".")]
					try:
						jsonData = table.Table(self.folder.getPath()+"/"+file)
						retDict[key] = jsonData
					except:
						pass

		return  retDict

	def getData(self, table):
		return self.tables[str(table)]




