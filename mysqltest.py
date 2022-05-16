#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql.cursors
connection = pymysql.connect(host='localhost', port=3306, user='root', password='56986041', db='TESTDB', charset= 'utf8mb4', cursorclass=pymysql.cursors.DictCursor)
try:
    cursor = connection.cursor()
    sql = "select * from EMPLOYEE"
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data)
except Exception:
    print('查询失败')
    pass
cursor.close()
connection.close()