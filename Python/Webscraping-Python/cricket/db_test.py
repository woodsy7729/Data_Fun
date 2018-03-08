#!/usr/bin/python
import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='woodsy7729', password='', database='test')
cursor = mariadb_connection.cursor()
#sql = '''
#CREATE TABLE nutanix(
#    name char DEFAULT NULL
#)
#'''
sql = '''
INSERT INTO nutanix values ("w")

'''
cursor.execute(sql)
mariadb_connection.commit()
mariadb_connection.close()
