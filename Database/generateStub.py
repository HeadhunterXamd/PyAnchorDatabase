__author__ = 'Niels'
from json import *
import random


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


for x in range(5):
	f = open(str(x)+".table", "w")
	table = generateRandomTable(15)
	dump(table, f)