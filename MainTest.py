__author__ = 'Niels'

from Database.DataManager import *

d = DataManager('mongodb://localhost:27017/')


print(d.getData())
# print(d.getData().keys[0])
