import MySQLdb

conn=MySQLdb.connect(user='root',password='',host='localhost',database='Your_databse_name')
mycursor=conn.cursor()
mycursor.execute('SQL Query') #SQL command must be in line
print(mycursor.fetchall()) #Result comes after executing mycursor

#Keep your database server active before connecting

conn.close()
