__author__ = 'niels'
from pymongo import MongoClient

class Database():

	def __init__(self, addres:str):
		self.client = MongoClient(addres)
		self.db = None

	def __repr__(self):
		pass