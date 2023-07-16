import mysql.connector
cnx = mysql.connector.connect(user='root', password='Mohammad123', host='127.0.0.1', database='employees')
cursor=cnx.cursor()
query='SELECT * FROM employees ORDER BY Height DESC, Weight ASC;'
cursor.execute(query)
for (Name, Weight, Height) in cursor:
    print('%s %s %s' %(Name, Height, Weight))
cursor.close()
cnx.close()