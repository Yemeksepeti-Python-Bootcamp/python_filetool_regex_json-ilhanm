from DbOperations import DbOperations
from DataParser import DataParser

dp=DataParser("dataregex.json")
allusers=dp.createUsersFromJSON()

dbops=DbOperations("users.db")
dbops.createTable()
dbops.insertUserList(allusers)