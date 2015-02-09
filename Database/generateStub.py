__author__ = 'Niels'
from json import *
import random
from pymongo import MongoClient

def generateRandomString(length:int):
	s = " aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789"
	retString = ""
	for x in range(length):
		retString += s[random.randint(0, len(s)-1)]

	return retString


def generateRandomTable(length):
	table = {}

	for x in range(length):
		key = generateRandomString(5)
		value = generateRandomString(15)
		table[key] = value

	return table

client = MongoClient('mongodb://localhost:27017/')
db = client.mydb

for x in range(5):
	table = generateRandomTable(500)
	db.data.insert(table)

print(db.collection_names())