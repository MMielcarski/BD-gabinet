import mysql.connector
import haslo
mydb = mysql.connector.connect(    #struktura potrzebna do laczenia z baza
    host=" db4free.net",
    user ="root00",
    passwd =haslo.haslo(),   #utworz plik (nie dodawaj na gita) i tam funckje haslo() ktora zaraca haslo
    database = "dbgabinet"
)


mycursor = mydb.cursor()    #utworzenie kursora potrzebnego do poruszania się po bazie (selecty, inserty itp)

# mycursor.execute("SHOW DATABASES") #pokazywanie dostepnych baz danych

# mycursor.execute("SHOW TABLES")  # pokazywanie dostepnych tabel w bazie z ktorą jesteśmy polaczeni
# for x in mycursor:
#    print(x)

sql = "SELECT ID_LEKARZA FROM lekarze WHERE adres_email = 'mp@re.pl' AND haslo = 'admin1'"
print(sql)

# mycursor.execute("SHOW DATABASES")  # pokazywanie dostepnych baz danych
# for x in mycursor:
#     print(x)

mycursor.execute("SELECT imie FROM lekarze WHERE adres_email = 'sklodowski_pediatra@gmail.com' AND haslo = 'admin2'")

myresult = mycursor.fetchall()
print(myresult)
print(myresult[0])

for x in myresult:
  print(x[0])



#tworzenie SELECTÓW



mydb.close()
