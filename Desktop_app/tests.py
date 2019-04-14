import mysql.connector

mydb = mysql.connector.connect(
    host=" db4free.net",
    user ="root00",
    passwd ="!!!!",
    database = "dbgabinet"
)


print(mydb)
mydb.close()
