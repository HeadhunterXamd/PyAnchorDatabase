__author__ = 'Niels'

import folderStructure.folder as folder
from json import *



class DataManager():

	def __init__(self):
		self.folder = folder.Folder(__file__)
		self.tables = self.getTables()


	def getTables(self)->dict:
		retDict = {}
		files = self.folder.getFiles()
		for file in files:
			if ".py" not in file:
				f = open(self.folder.getPath()+"/"+file, "r")
				key = file[:file.index(".")]
				try:
					jsonData = load(f)
					retDict[key] = jsonData
				except:
					pass

		return  retDict

	def getData(self, table):
		return self.tables[str(table)]




