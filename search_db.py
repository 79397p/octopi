import mysql.connector
def connect(u = 'root', pw = '', h = 'localhost', n = "test"):
    cnx = mysql.connector.connect(user = u, password = pw, host = h, database = n)
    return cnx

cnx = connect(n = "test")
cursor = cnx.cursor()

def search(searchString): #search for single word
    cursor.execute("SELECT storedValue FROM Map WHERE keyWord = '%s'" %searchString)
    storedValues = [value for value in cursor]
    return storedValues

print search('octopi')
print search('fishing')

cursor.close()
cnx.close()
