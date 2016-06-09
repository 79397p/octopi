#this file is just to experiment with python and connector/python
#install connector/python on fedora/linux with the following command:
#sudo yum install mysql-connector-python
#helpfull resource: https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html


#Cheat Sheet:
#import mysql.connector #what you just installed on your system
#
#
#connect to mysql server:
#cnx = mysql.connector.connect(user='uname', password='pswrd',
#                              host='127.0.0.1',
#                              database='database_name')
#
#whatever this is:
#cursor = cnx.cursor()
#
#interact with database:
#cursor.execute(<SQL command>)
#
#commit changes:
#cnx.commit()
#
#read from cursor after query:
#for (t1, t2, t3) in cursor:
#    print t1, t2, t3
#
#remember to close the cursor (whatever that does):
#cursor.close()
#
#and to close the connector:
#cnx.close()
#
#That is it. Have fun!
