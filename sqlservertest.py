import pymssql
# import pymssql.cursors
host = '192.168.1.16'
user = 'sa'
password = '56986041'
database = 'pd_sys'

conn = pymssql.connect(host=host,user=user,password=password,database=database)
cursor = conn.cursor()
cursor.execute('select * from t_yh')
result = cursor.fetchall()
for data in result:
    print(data)

cursor.close()
conn.close()